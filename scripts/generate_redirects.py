#!/usr/bin/env python3
"""Generate redirect mappings from old WordPress URLs to new MkDocs blog URLs.

Old WordPress URL format: /{YYYY}/{MM}/{slug}/
New MkDocs blog URL format: /blog/{YYYY}/{MM}/{DD}/{slug}/

This script scans docs/blog/posts/*.md, extracts dates and titles,
and outputs a YAML snippet for mkdocs.yml redirect_maps.
"""

import re
from pathlib import Path

from pymdownx.slugs import slugify

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "docs" / "blog" / "posts"

slugify_fn = slugify(case="lower")


def extract_post_info(filepath: Path) -> dict | None:
    """Extract date and title from a blog post markdown file."""
    text = filepath.read_text(encoding="utf-8")

    date_match = re.search(r"^date:\s*(\d{4}-\d{2}-\d{2})", text, re.MULTILINE)
    if not date_match:
        return None
    year, month, day = date_match.group(1).split("-")

    title_match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if not title_match:
        return None
    title = title_match.group(1).strip()

    filename_slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", filepath.stem)
    mkdocs_slug = slugify_fn(title, "-")

    return {
        "year": year,
        "month": month,
        "day": day,
        "filename_slug": filename_slug,
        "mkdocs_slug": mkdocs_slug,
    }


def main():
    posts = sorted(POSTS_DIR.glob("*.md"))
    redirect_maps = {}

    for post_path in posts:
        info = extract_post_info(post_path)
        if not info:
            print(f"WARNING: Could not extract info from {post_path.name}")
            continue

        year, month, day = info["year"], info["month"], info["day"]
        old_path = f"{year}/{month}/{info['filename_slug']}.md"
        new_url = f"https://mindwerks.net/blog/{year}/{month}/{day}/{info['mkdocs_slug']}/"
        redirect_maps[old_path] = new_url

    # Write the redirect_maps as a YAML snippet
    yaml_path = ROOT / "scripts" / "redirect_maps.yml"
    with open(yaml_path, "w", encoding="utf-8") as f:
        f.write("# Generated redirect mappings - copy into mkdocs.yml\n")
        f.write("# under plugins > redirects > redirect_maps\n")
        for old, new in sorted(redirect_maps.items()):
            f.write(f"        '{old}': '{new}'\n")
    print(f"Wrote {len(redirect_maps)} entries to {yaml_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
