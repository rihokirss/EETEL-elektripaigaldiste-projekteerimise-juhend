# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Estonian electrical installations design guide (Elektripaigaldiste projekteerimise juhend) by EETEL. Built with MkDocs Material theme, served as static site on port 8080 via systemd user service. Content is in Estonian.

## Build Commands

```bash
# Development server (live reload)
source .venv/bin/activate && mkdocs serve

# Build HTML only (fast)
source .venv/bin/activate && mkdocs build

# Build HTML + PDF (slow, ~16s)
source .venv/bin/activate && ENABLE_PDF_EXPORT=1 mkdocs build

# Restart web server after build
systemctl --user restart elektrijuhend
```

**Important:** Running `mkdocs build` without `ENABLE_PDF_EXPORT=1` deletes the PDF from `site/`. Always use the env var when PDF is needed.

## Architecture

### Styling pipeline
- **Web:** `docs/stylesheets/extra.css` → CSS variables for Material theme (light + dark mode)
- **PDF plugin styles:** `templates/styles.scss` → compiled by mkdocs-with-pdf after its own SCSS, overrides plugin defaults (red heading lines → EETEL blue)
- **PDF legacy:** `docs/stylesheets/pdf.css` → not loaded by plugin, kept for reference only
- **PDF cover:** `templates/cover.html.j2` → custom Jinja2 template using `<img>` tag (WeasyPrint doesn't support CSS `background-image`)

### PDF generation
Plugin `mkdocs-with-pdf` uses WeasyPrint. Key quirks:
- `custom_template_path: templates` in mkdocs.yml points to `templates/` dir for `cover.html.j2` and `styles.scss`
- `ordered_chapter_level: 0` disables auto-numbering (nav labels already have numbers)
- Plugin compiles SCSS in order: its own styles → `templates/styles.scss`, so our file can override defaults

### Brand colors (from EETEL logo SVG)
- Primary: `#1c60a9` (logo arc)
- Dark: `#03325e` (logo text)
- Accent: `#407cc6` (derived lighter variant)
- Dark mode backgrounds: `#16242e`, `#1c2d38`, `#223644`

### Logo files
- `docs/_assets/media/eetel_logo.svg` — all-white version for dark header
- `docs/_assets/media/eetel_logo_color.svg` — original colors
- `docs/_assets/media/eetel_logo_color.png` — high-DPI raster (600 DPI) for PDF cover

### Content chapters
Sections marked with `*` in nav (e.g., `Nõrkvool*`) are still in development. Chapters 1-5, 7-8 have content. Markdown files use Estonian lowercase title rules.

### Fonts (PDF only)
Inter + Inter Display for text/headings, JetBrains Mono for code. Installed in `~/.local/share/fonts/`.

## Deployment

Static site served by Python HTTP server on port 8080. Systemd user service at `~/.config/systemd/user/elektrijuhend.service`. Reverse proxy handled externally.
