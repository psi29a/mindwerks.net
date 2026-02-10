# Mindwerks.net

A MkDocs-based static website using the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme.

## Setup

```bash
./setup_venv.sh
```

## Development

```bash
source .venv/bin/activate
mkdocs serve
```

Then open http://127.0.0.1:8080 in your browser.

## Build

```bash
mkdocs build
```

## Site Structure

```
docs/
├── index.md                  # Homepage
├── blog/
│   └── posts/                # Blog posts (auto-indexed by date)
│       └── YYYY-MM-DD-slug.md
├── assets/
│   └── images/               # Images organized by YYYY/MM/
│       └── YYYY/MM/file.ext
├── about.md                  # About page
├── wildmidi.md               # Project pages...
└── ...                       # Other static pages
```

## Writing a New Blog Post

1. Create a new Markdown file in `docs/blog/posts/` with the naming convention:

   ```
   docs/blog/posts/YYYY-MM-DD-your-post-slug.md
   ```

2. Add front matter at the top of the file:

   ```yaml
   ---
   date: 2026-02-10
   categories:
     - Linux
   tags:
     - ubuntu
     - networking
   ---
   ```

3. Write your content below the front matter using standard Markdown:

   ```markdown
   # Your Post Title

   Your content here. Use standard Markdown syntax.

   ## Subheading

   More content...
   ```

4. To add images, place them in `docs/assets/images/` and reference them with:

   ```markdown
   ![Alt text](/assets/images/your-image.png)
   ```

5. Preview with `mkdocs serve` — the blog plugin will automatically add your post to the blog index, archive, and category pages.

## Adding a New Page

1. Create a new Markdown file in `docs/`:

   ```
   docs/your-page.md
   ```

2. Write your content using standard Markdown (no front matter required for pages):

   ```markdown
   # Page Title

   Your content here.
   ```

3. Add the page to the navigation in `mkdocs.yml` under the appropriate section:

   ```yaml
   nav:
     - Projects:
       - Your New Page: your-page.md
   ```

## Available Categories

Categories used across the blog: Linux, Ubuntu, Debian, Code, C/C++, Hardware, Laptop, Video, Servers, Storage, Software, Python, Operating Systems.

You can use any of these or create new ones in your post front matter.
