#!/usr/bin/env python3
"""
WordPress to MkDocs migration script for mindwerks.net

Parses a WordPress MySQL dump and wp-content uploads directory,
converting posts to MkDocs blog entries and pages to regular MkDocs pages.
"""

import html
import os
import re
import shutil
import sqlite3
from datetime import datetime
from pathlib import Path

from bs4 import BeautifulSoup
from markdownify import markdownify as md, MarkdownConverter

# === Configuration ===
SQL_DUMP = "/tmp/mindwerks/mindwerks_20151007.sql"
WP_UPLOADS = "/tmp/mindwerks/srv/www/www.mindwerks.net/public/wp-content/uploads"
OUTPUT_DIR = Path("docs")
BLOG_DIR = OUTPUT_DIR / "blog" / "posts"
PAGES_DIR = OUTPUT_DIR
IMAGES_DIR = OUTPUT_DIR / "assets" / "images"
TABLE_PREFIX = "mw_"

# WordPress URL patterns to rewrite
WP_URL_PATTERNS = [
    r"https?://(?:www\.)?mindwerks\.net/wp-content/uploads/",
    r"/wp-content/uploads/",
]

# Binary file extensions to redirect to Wayback Machine instead of serving locally
BINARY_EXTENSIONS = {".zip", ".tar.gz", ".tar.bz2", ".pdf", ".esm.tar.gz"}

# Wayback Machine base URL for binary downloads
WAYBACK_BASE = "https://web.archive.org/web/2015/https://mindwerks.net/wp-content/uploads"


def rewrite_binary_links_to_wayback(markdown):
    """Rewrite links to binary files (.zip, .tar.gz, .pdf, etc.) to Wayback Machine URLs."""
    def replace_binary_link(m):
        _ = m.group(1)  # the relative path prefix (discarded, replaced with Wayback URL)
        year = m.group(2)
        month = m.group(3)
        filename = m.group(4)
        return f"{WAYBACK_BASE}/{year}/{month}/{filename}"

    # Match links to binary files in both blog post and page relative paths
    for prefix in [r"\.\.\/\.\.\/assets\/images\/", r"assets\/images\/"]:
        markdown = re.sub(
            r"(" + prefix + r")(\d{4})/(\d{2})/([^\s\)\"]+\.(?:zip|tar\.gz|tar\.bz2|pdf|esm\.tar\.gz))",
            replace_binary_link,
            markdown,
        )
    return markdown


class CustomConverter(MarkdownConverter):
    """Custom markdownify converter to handle WordPress-specific HTML."""

    def convert_pre(self, el, text, convert_as_inline):
        """Handle <pre> blocks, often used for code in WordPress."""
        # Try to detect language from class
        lang = ""
        code_el = el.find("code")
        classes = el.get("class", []) or (code_el.get("class", []) if code_el else [])
        if classes:
            for cls in classes:
                if cls.startswith("language-") or cls.startswith("lang-"):
                    lang = cls.split("-", 1)[1]
                    break
                elif cls in ("bash", "python", "c", "cpp", "java", "xml", "html",
                             "css", "javascript", "json", "sql", "php", "shell"):
                    lang = cls
                    break
        # Get raw text content
        code_text = el.get_text()
        return f"\n```{lang}\n{code_text}\n```\n"


def preprocess_wp_images(html_content, image_prefix):
    """
    Pre-process WordPress aligned images in HTML before markdownify conversion.

    Detects <img> tags with WordPress alignment classes (alignleft, alignright,
    aligncenter) and converts them to Markdown with Material theme attributes.
    Handles both linked thumbnails (wrapped in <a>) and standalone images.

    Uses placeholders to prevent markdownify from escaping the Markdown syntax.

    Args:
        html_content: Raw WordPress HTML
        image_prefix: Relative path prefix for images (e.g., "../../assets/images/"
                      for blog posts or "assets/images/" for pages)

    Returns:
        Tuple of (modified HTML, dict of placeholder->markdown replacements)
    """
    soup = BeautifulSoup(html_content, "html.parser")
    placeholders = {}
    counter = 0

    for img in soup.find_all("img"):
        # Skip images already detached from tree (e.g., inside a replaced <a>)
        if not img.parent:
            continue
        classes = img.get("class", [])
        if not classes:
            continue

        # Determine alignment
        alignment = None
        for cls in classes:
            if cls == "alignleft":
                alignment = "left"
            elif cls == "alignright":
                alignment = "right"
            elif cls == "aligncenter":
                alignment = "center"
        if not alignment:
            continue

        # Get image attributes
        src = img.get("src", "")
        alt = img.get("alt", "") or img.get("title", "") or ""
        width = img.get("width", "")

        # Determine the width attribute for Material theme
        is_thumbnail = "size-thumbnail" in classes
        is_medium = "size-medium" in classes
        if is_thumbnail:
            width_attr = "200"
        elif is_medium and width:
            width_attr = width
        elif width and int(width) < 400:
            width_attr = width
        else:
            width_attr = ""

        # Build the Material attribute string
        attrs = []
        if alignment in ("left", "right"):
            attrs.append(f"align={alignment}")
        if width_attr:
            attrs.append(f"width=\"{width_attr}\"")
        attr_str = "{ " + " ".join(attrs) + " }" if attrs else ""

        # Rewrite the image src to local path
        local_src = src
        for pattern in WP_URL_PATTERNS:
            local_src = re.sub(
                pattern + r"(\d{4})/(\d{2})/([^\s\)\"]+?)-\d+x\d+\.(\w+)",
                image_prefix + r"\1/\2/\3.\4",
                local_src,
            )
            local_src = re.sub(
                pattern + r"(\d{4})/(\d{2})/([^\s\)\"]+)",
                image_prefix + r"\1/\2/\3",
                local_src,
            )

        # Build Markdown image with Material attributes.
        # Always use Markdown syntax (not raw HTML) so MkDocs rewrites
        # relative paths correctly for the final URL structure.
        md_img = f"\n\n![{alt}]({local_src})"
        if attr_str:
            md_img += attr_str
        md_img += "\n\n"

        placeholder = f"WPIMGPLACEHOLDER{counter}ENDPLACEHOLDER"
        counter += 1
        placeholders[placeholder] = md_img

        # Remove parent <a> wrapper if present (linked thumbnail)
        parent = img.parent
        if parent and parent.name == "a":
            parent.replace_with(placeholder)
        else:
            img.replace_with(placeholder)

    return str(soup), placeholders


def mysql_to_sqlite(sql_path):
    """Load a MySQL dump into an in-memory SQLite database."""
    with open(sql_path, "r", encoding="utf-8", errors="replace") as f:
        sql = f.read()

    # Strip MySQL-specific syntax for SQLite compatibility
    sql = re.sub(r"/\*!.*?\*/;?\s*", "", sql)
    sql = re.sub(r"LOCK TABLES.*?;\s*", "", sql)
    sql = re.sub(r"UNLOCK TABLES;\s*", "", sql)
    sql = re.sub(r"KEY\s+`[^`]*`\s*\([^)]*\),?\s*", "", sql)
    sql = re.sub(r"UNIQUE KEY\s+`[^`]*`\s*\([^)]*\),?\s*", "", sql)
    sql = re.sub(r"ENGINE=\w+.*?;", ";", sql)
    sql = re.sub(r"unsigned", "", sql)
    sql = re.sub(r"AUTO_INCREMENT", "", sql)
    # Handle MySQL escaped quotes
    sql = re.sub(r"\\\\", "DBLBACKSLASH", sql)
    sql = re.sub(r"\\'", "''", sql)
    sql = re.sub(r"DBLBACKSLASH", "\\\\", sql)
    # Remove trailing commas before closing parens in CREATE TABLE
    sql = re.sub(r",\s*\n\s*\)", "\n)", sql)

    db = sqlite3.connect(":memory:")
    db.executescript(sql)
    return db


def parse_sql_manual(sql_path):
    """
    Fallback parser: manually extract INSERT values from the SQL dump
    using a state machine approach (handles complex escaped content).
    """
    with open(sql_path, "r", encoding="utf-8", errors="replace") as f:
        lines = f.readlines()

    tables = {}
    for line in lines:
        match = re.match(r"INSERT INTO `(\w+)` VALUES ", line)
        if not match:
            continue
        table_name = match.group(1)
        values_str = line[match.end():].rstrip(";\n")

        # Parse records using state machine
        records = []
        current = []
        in_string = False
        escape_next = False
        depth = 0

        for ch in values_str:
            if escape_next:
                current.append(ch)
                escape_next = False
                continue
            if ch == "\\":
                current.append(ch)
                escape_next = True
                continue
            if ch == "'" and not escape_next:
                in_string = not in_string
                current.append(ch)
                continue
            if not in_string:
                if ch == "(":
                    depth += 1
                    if depth == 1:
                        current = []
                        continue
                elif ch == ")":
                    depth -= 1
                    if depth == 0:
                        records.append("".join(current))
                        continue
                elif ch == "," and depth == 0:
                    continue
            current.append(ch)

        if table_name not in tables:
            tables[table_name] = []
        tables[table_name].extend(records)

    return tables


def parse_record_fields(record_str):
    """Parse a single SQL VALUES record into a list of field values."""
    fields = []
    current_field = []
    in_str = False
    esc = False

    for ch in record_str:
        if esc:
            current_field.append(ch)
            esc = False
            continue
        if ch == "\\":
            current_field.append(ch)
            esc = True
            continue
        if ch == "'":
            in_str = not in_str
            continue  # strip quotes
        if ch == "," and not in_str:
            fields.append("".join(current_field).strip())
            current_field = []
            continue
        current_field.append(ch)
    fields.append("".join(current_field).strip())
    return fields


def unescape_mysql(text):
    """Unescape MySQL string escapes."""
    text = text.replace("\\'", "'")
    text = text.replace('\\"', '"')
    text = text.replace("\\n", "\n")
    text = text.replace("\\r", "")
    text = text.replace("\\t", "\t")
    text = text.replace("\\\\", "\\")
    return text


def extract_posts_and_pages(tables):
    """Extract published posts and pages from parsed SQL data."""
    posts = []
    pages = []

    # mw_posts columns (WordPress 3.x/4.x):
    # 0:ID 1:post_author 2:post_date 3:post_date_gmt 4:post_content
    # 5:post_title 6:post_excerpt 7:post_status 8:comment_status
    # 9:ping_status 10:post_password 11:post_name 12:to_ping
    # 13:pinged 14:post_modified 15:post_modified_gmt
    # 16:post_content_filtered 17:post_parent 18:guid
    # 19:menu_order 20:post_type 21:post_mime_type 22:comment_count

    for record_str in tables.get(f"{TABLE_PREFIX}posts", []):
        fields = parse_record_fields(record_str)
        if len(fields) < 21:
            continue

        post_id = fields[0]
        post_date = fields[2]
        post_content = unescape_mysql(fields[4])
        post_title = unescape_mysql(fields[5])
        post_excerpt = unescape_mysql(fields[6])
        post_status = fields[7]
        post_name = fields[11]  # slug
        post_type = fields[20]

        if post_status != "publish":
            continue

        entry = {
            "id": int(post_id),
            "date": post_date,
            "content": post_content,
            "title": post_title,
            "excerpt": post_excerpt,
            "slug": post_name,
            "type": post_type,
        }

        if post_type == "post":
            posts.append(entry)
        elif post_type == "page":
            pages.append(entry)

    return posts, pages


def extract_terms(tables):
    """Extract categories and tags, and their relationships to posts."""
    # mw_terms: term_id, name, slug, term_group
    terms = {}
    for record_str in tables.get(f"{TABLE_PREFIX}terms", []):
        fields = parse_record_fields(record_str)
        if len(fields) >= 3:
            terms[fields[0]] = {"name": unescape_mysql(fields[1]), "slug": fields[2]}

    # mw_term_taxonomy: term_taxonomy_id, term_id, taxonomy, description, parent, count
    taxonomies = {}
    for record_str in tables.get(f"{TABLE_PREFIX}term_taxonomy", []):
        fields = parse_record_fields(record_str)
        if len(fields) >= 6:
            tt_id = fields[0]
            term_id = fields[1]
            taxonomy = fields[2]
            if term_id in terms:
                taxonomies[tt_id] = {
                    "term_id": term_id,
                    "taxonomy": taxonomy,
                    "name": terms[term_id]["name"],
                    "slug": terms[term_id]["slug"],
                }

    # mw_term_relationships: object_id (post_id), term_taxonomy_id, term_order
    post_categories = {}  # post_id -> [category names]
    post_tags = {}  # post_id -> [tag names]
    for record_str in tables.get(f"{TABLE_PREFIX}term_relationships", []):
        fields = parse_record_fields(record_str)
        if len(fields) >= 2:
            post_id = fields[0]
            tt_id = fields[1]
            if tt_id in taxonomies:
                tax = taxonomies[tt_id]
                if tax["taxonomy"] == "category":
                    post_categories.setdefault(post_id, []).append(tax["name"])
                elif tax["taxonomy"] == "post_tag":
                    post_tags.setdefault(post_id, []).append(tax["name"])

    return post_categories, post_tags


def convert_html_to_markdown(html_content):
    """Convert WordPress HTML content to clean Markdown."""
    if not html_content or not html_content.strip():
        return ""

    # Handle WordPress shortcodes before conversion
    # [caption] shortcode
    html_content = re.sub(
        r'\[caption[^\]]*\](.*?)\[/caption\]',
        r'\1',
        html_content,
        flags=re.DOTALL,
    )

    # [code] or [sourcecode] shortcodes -> <pre><code>
    def replace_code_shortcode(m):
        attrs = m.group(1)
        code = html.escape(m.group(2))
        lang = ""
        lang_match = re.search(r'language=["\']?(\w+)', attrs)
        if lang_match:
            lang = lang_match.group(1)
        elif re.search(r'lang=["\']?(\w+)', attrs):
            lang = re.search(r'lang=["\']?(\w+)', attrs).group(1)
        return f'<pre><code class="language-{lang}">{code}</code></pre>'

    html_content = re.sub(
        r'\[(?:sourcecode|code)([^\]]*)\](.*?)\[/(?:sourcecode|code)\]',
        replace_code_shortcode,
        html_content,
        flags=re.DOTALL,
    )

    # Language-name shortcodes: [shell]...[/shell], [python]...[/python], etc.
    # These are used by WordPress syntax highlighter plugins
    def replace_lang_shortcode(m):
        lang = m.group(1)
        code = html.escape(m.group(2))
        # Map shortcode names to markdown language identifiers
        lang_map = {"shell": "bash", "c": "c", "python": "python", "bash": "bash"}
        lang = lang_map.get(lang, lang)
        return f'<pre><code class="language-{lang}">{code}</code></pre>'

    html_content = re.sub(
        r'\[(shell|bash|python|c)\](.*?)\[/\1\]',
        replace_lang_shortcode,
        html_content,
        flags=re.DOTALL,
    )

    # Strip remaining shortcodes
    html_content = re.sub(r'\[\/?[a-zA-Z_]+[^\]]*\]', '', html_content)

    # Convert <blockquote><code>...</code></blockquote> to <pre><code>...</code></pre>
    # WordPress users often used blockquotes for code blocks
    html_content = re.sub(
        r'<blockquote>\s*<code>(.*?)</code>\s*</blockquote>',
        r'<pre><code>\1</code></pre>',
        html_content,
        flags=re.DOTALL,
    )

    # WordPress uses double newlines for paragraphs in non-HTML content
    # (wpautop behavior) - wrap plain text paragraphs in <p> tags
    if "<p>" not in html_content.lower() and "<div>" not in html_content.lower() and "<pre>" not in html_content.lower():
        paragraphs = html_content.split("\n\n")
        html_content = "".join(f"<p>{p.strip()}</p>" for p in paragraphs if p.strip())

    # Pre-process WordPress aligned images before markdownify conversion
    html_content, img_placeholders = preprocess_wp_images(html_content, "../../assets/images/")

    # Convert using our custom converter
    markdown = md(
        html_content,
        heading_style="atx",
        bullets="-",
        code_language="",
        strip=["script", "style"],
    )

    # Restore image placeholders with actual Markdown
    for placeholder, md_img in img_placeholders.items():
        markdown = markdown.replace(placeholder, md_img)

    # Clean up the markdown
    # Fix excessive blank lines
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    # Fix image references - rewrite WordPress URLs to local paths
    # Blog posts are at docs/blog/posts/, so relative path is ../../assets/images/
    for pattern in WP_URL_PATTERNS:
        # Handle thumbnail URLs first (e.g., image-300x200.jpg -> image.jpg)
        markdown = re.sub(
            pattern + r"(\d{4})/(\d{2})/([^\s\)\"]+?)-\d+x\d+\.(\w+)",
            r"../../assets/images/\1/\2/\3.\4",
            markdown,
        )
        markdown = re.sub(
            pattern + r"(\d{4})/(\d{2})/([^\s\)\"]+)",
            r"../../assets/images/\1/\2/\3",
            markdown,
        )
    # Rewrite binary download links to Wayback Machine
    markdown = rewrite_binary_links_to_wayback(markdown)

    # Also handle any remaining absolute mindwerks.net URLs in links
    markdown = re.sub(
        r"https?://(?:www\.)?mindwerks\.net/(?!wp-content)([^\s\)\"]+)",
        r"https://mindwerks.net/\1",  # keep external links as-is for now
        markdown,
    )

    return markdown.strip()


def convert_page_html_to_markdown(html_content):
    """Convert WordPress HTML content to Markdown for pages (different image paths)."""
    if not html_content or not html_content.strip():
        return ""

    # Same shortcode handling as posts
    html_content = re.sub(
        r'\[caption[^\]]*\](.*?)\[/caption\]',
        r'\1',
        html_content,
        flags=re.DOTALL,
    )

    def replace_code_shortcode(m):
        attrs = m.group(1)
        code = html.escape(m.group(2))
        lang = ""
        lang_match = re.search(r'language=["\']?(\w+)', attrs)
        if lang_match:
            lang = lang_match.group(1)
        elif re.search(r'lang=["\']?(\w+)', attrs):
            lang = re.search(r'lang=["\']?(\w+)', attrs).group(1)
        return f'<pre><code class="language-{lang}">{code}</code></pre>'

    html_content = re.sub(
        r'\[(?:sourcecode|code)([^\]]*)\](.*?)\[/(?:sourcecode|code)\]',
        replace_code_shortcode,
        html_content,
        flags=re.DOTALL,
    )

    # Language-name shortcodes: [shell]...[/shell], [python]...[/python], etc.
    def replace_lang_shortcode(m):
        lang = m.group(1)
        code = html.escape(m.group(2))
        lang_map = {"shell": "bash", "c": "c", "python": "python", "bash": "bash"}
        lang = lang_map.get(lang, lang)
        return f'<pre><code class="language-{lang}">{code}</code></pre>'

    html_content = re.sub(
        r'\[(shell|bash|python|c)\](.*?)\[/\1\]',
        replace_lang_shortcode,
        html_content,
        flags=re.DOTALL,
    )

    html_content = re.sub(r'\[\/?[a-zA-Z_]+[^\]]*\]', '', html_content)

    # Convert <blockquote><code>...</code></blockquote> to <pre><code>...</code></pre>
    html_content = re.sub(
        r'<blockquote>\s*<code>(.*?)</code>\s*</blockquote>',
        r'<pre><code>\1</code></pre>',
        html_content,
        flags=re.DOTALL,
    )

    if "<p>" not in html_content.lower() and "<div>" not in html_content.lower() and "<pre>" not in html_content.lower():
        paragraphs = html_content.split("\n\n")
        html_content = "".join(f"<p>{p.strip()}</p>" for p in paragraphs if p.strip())

    # Pre-process WordPress aligned images before markdownify conversion
    html_content, img_placeholders = preprocess_wp_images(html_content, "assets/images/")

    markdown = md(
        html_content,
        heading_style="atx",
        bullets="-",
        code_language="",
        strip=["script", "style"],
    )

    # Restore image placeholders with actual Markdown
    for placeholder, md_img in img_placeholders.items():
        markdown = markdown.replace(placeholder, md_img)

    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    # Pages are at docs/ level, so relative path is assets/images/
    for pattern in WP_URL_PATTERNS:
        # Handle thumbnail URLs first
        markdown = re.sub(
            pattern + r"(\d{4})/(\d{2})/([^\s\)\"]+?)-\d+x\d+\.(\w+)",
            r"assets/images/\1/\2/\3.\4",
            markdown,
        )
        markdown = re.sub(
            pattern + r"(\d{4})/(\d{2})/([^\s\)\"]+)",
            r"assets/images/\1/\2/\3",
            markdown,
        )

    # Rewrite binary download links to Wayback Machine
    markdown = rewrite_binary_links_to_wayback(markdown)

    return markdown.strip()


def copy_uploads(wp_uploads_dir, images_dir):
    """
    Copy non-binary files from wp-content/uploads to the MkDocs assets directory,
    preserving YYYY/MM structure. Binary downloads (.zip, .tar.gz, .pdf, etc.)
    are redirected to the Wayback Machine in the Markdown content instead.
    """
    wp_uploads = Path(wp_uploads_dir)
    images_out = Path(images_dir)
    copied = 0
    skipped = 0
    binaries_skipped = 0

    for src_file in wp_uploads.rglob("*"):
        if not src_file.is_file():
            continue
        # Skip WordPress-generated thumbnails (e.g., image-150x150.png)
        if re.search(r"-\d+x\d+\.", src_file.name):
            skipped += 1
            continue
        # Skip shadowbox-js plugin assets and ithemes-security
        if "shadowbox-js" in str(src_file) or "ithemes-security" in str(src_file):
            continue
        # Skip binary files (served via Wayback Machine links instead)
        name_lower = src_file.name.lower()
        if any(name_lower.endswith(ext) for ext in BINARY_EXTENSIONS):
            binaries_skipped += 1
            continue

        # Preserve the YYYY/MM/filename structure
        try:
            rel_path = src_file.relative_to(wp_uploads)
        except ValueError:
            continue

        dest = images_out / rel_path
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_file, dest)
        copied += 1

    print(f"  Copied {copied} files (skipped {skipped} thumbnails, {binaries_skipped} binaries -> Wayback Machine)")
    return copied


def write_blog_post(post, categories, tags, output_dir):
    """Write a single blog post as a MkDocs blog Markdown file."""
    date_str = post["date"][:10]  # YYYY-MM-DD
    slug = post["slug"]
    title = post["title"]

    # Build front matter
    front_matter = f'---\ndate: {date_str}\n'

    if categories:
        front_matter += "categories:\n"
        for cat in categories:
            if cat != "Uncategorized":
                front_matter += f"  - {cat}\n"

    if tags:
        front_matter += "tags:\n"
        for tag in tags:
            front_matter += f"  - {tag}\n"

    front_matter += "---\n\n"

    # Convert content
    markdown_content = convert_html_to_markdown(post["content"])

    # Build the file
    file_content = front_matter
    file_content += f"# {title}\n\n"
    file_content += markdown_content + "\n"

    # Filename: YYYY-MM-DD-slug.md
    filename = f"{date_str}-{slug}.md"
    filepath = output_dir / filename
    filepath.parent.mkdir(parents=True, exist_ok=True)
    filepath.write_text(file_content, encoding="utf-8")
    return filepath


def write_page(page, output_dir):
    """Write a static page as a MkDocs Markdown file."""
    slug = page["slug"]
    title = page["title"]

    markdown_content = convert_page_html_to_markdown(page["content"])

    file_content = f"# {title}\n\n"
    file_content += markdown_content + "\n"

    filename = f"{slug}.md"
    filepath = output_dir / filename
    filepath.parent.mkdir(parents=True, exist_ok=True)
    filepath.write_text(file_content, encoding="utf-8")
    return filepath


def main():
    print("=== WordPress to MkDocs Migration ===\n")

    # Step 1: Parse SQL dump
    print("Parsing SQL dump...")
    tables = parse_sql_manual(SQL_DUMP)
    print(f"  Found tables: {', '.join(sorted(tables.keys()))}")

    # Step 2: Extract content
    print("\nExtracting posts and pages...")
    posts, pages = extract_posts_and_pages(tables)
    print(f"  Found {len(posts)} published posts")
    print(f"  Found {len(pages)} published pages")

    # Step 3: Extract taxonomy
    print("\nExtracting categories and tags...")
    post_categories, post_tags = extract_terms(tables)

    # Step 4: Copy uploads (images, patches, archives, etc.)
    print(f"\nCopying uploads from {WP_UPLOADS}...")
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    copy_uploads(WP_UPLOADS, IMAGES_DIR)

    # Step 5: Create blog posts directory
    print(f"\nWriting blog posts to {BLOG_DIR}/...")
    BLOG_DIR.mkdir(parents=True, exist_ok=True)
    posts_sorted = sorted(posts, key=lambda p: p["date"])
    for post in posts_sorted:
        pid = str(post["id"])
        cats = post_categories.get(pid, [])
        tags = post_tags.get(pid, [])
        filepath = write_blog_post(post, cats, tags, BLOG_DIR)
        print(f"  [{post['date'][:10]}] {post['title'][:60]:60s} -> {filepath.name}")

    # Step 6: Write pages
    print(f"\nWriting pages to {PAGES_DIR}/...")
    # Skip certain pages that don't make sense in the new site
    skip_pages = {"archives", "sitemap"}
    for page in pages:
        if page["slug"] in skip_pages:
            print(f"  Skipping '{page['title']}' (not needed in MkDocs)")
            continue
        filepath = write_page(page, PAGES_DIR)
        print(f"  {page['title']:60s} -> {filepath.name}")

    # Summary
    print(f"\n=== Migration Complete ===")
    print(f"  Blog posts: {len(posts_sorted)}")
    print(f"  Pages: {len([p for p in pages if p['slug'] not in skip_pages])}")
    print(f"  Images: {IMAGES_DIR}")
    print(f"\nNext steps:")
    print(f"  1. Update mkdocs.yml with blog plugin config and nav")
    print(f"  2. Run 'mkdocs serve' to preview")
    print(f"  3. Review and fix any conversion artifacts")


if __name__ == "__main__":
    main()
