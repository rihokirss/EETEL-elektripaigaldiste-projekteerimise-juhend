#!/usr/bin/env python
"""Build a single .docx from MkDocs markdown sources, in mkdocs.yml nav order."""
from pathlib import Path
import re
import sys
import yaml
import pypandoc

ROOT = Path(__file__).parent.resolve()
DOCS = ROOT / "docs"
OUT = ROOT / "site" / "pdf" / "Elektripaigaldiste_Juhend.docx"


class IgnoreTagsLoader(yaml.SafeLoader):
    pass


def _ignore_tag(loader, tag_suffix, node):
    return None


IgnoreTagsLoader.add_multi_constructor("tag:yaml.org,2002:python/", _ignore_tag)
IgnoreTagsLoader.add_multi_constructor("!", _ignore_tag)


def collect_md_files(nav):
    """Walk mkdocs nav and yield (title, path) tuples in order."""
    out = []
    for item in nav:
        if isinstance(item, dict):
            for key, value in item.items():
                if isinstance(value, str):
                    out.append((key, DOCS / value))
                elif isinstance(value, list):
                    out.extend(collect_md_files(value))
        elif isinstance(item, str):
            out.append((None, DOCS / item))
    return out


FIGURE_RE = re.compile(
    r'<figure[^>]*>\s*!\[([^\]]*)\]\(([^)]+)\)\s*<figcaption>(.*?)</figcaption>\s*</figure>',
    re.DOTALL,
)
IMG_RE = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\s*\)")
IMG_ATTR_RE = re.compile(r"(!\[[^\]]*\]\([^)]+\))\{[^}]*\}")
ADMONITION_RE = re.compile(r"^(!!!|\?\?\?\+?)\s+\w+(?:\s+\"([^\"]*)\")?\s*$", re.MULTILINE)


def preprocess(text, src_dir):
    """Normalise markdown so pandoc can render it cleanly to docx."""
    text = FIGURE_RE.sub(
        lambda m: f"![{m.group(3).strip()}]({m.group(2).strip()})",
        text,
    )
    text = IMG_ATTR_RE.sub(r"\1", text)

    def fix_img(m):
        alt, path = m.group(1), m.group(2).strip()
        if path.startswith(("http://", "https://", "data:")):
            return m.group(0)
        resolved = (src_dir / path).resolve()
        try:
            return f"![{alt}]({resolved.relative_to(DOCS).as_posix()})"
        except ValueError:
            return m.group(0)

    text = IMG_RE.sub(fix_img, text)

    def admon(m):
        title = m.group(2)
        return f"> **{title}**" if title else "> **Märkus**"

    text = ADMONITION_RE.sub(admon, text)
    return text


def main():
    with open(ROOT / "mkdocs.yml") as f:
        config = yaml.load(f, Loader=IgnoreTagsLoader)

    files = collect_md_files(config["nav"])

    parts = []
    for _, path in files:
        if not path.exists():
            print(f"warn: {path} missing", file=sys.stderr)
            continue
        text = path.read_text()
        parts.append(preprocess(text, path.parent))
        parts.append("")

    combined = "\n\n".join(parts)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    pypandoc.convert_text(
        combined,
        "docx",
        format="markdown-yaml_metadata_block-multiline_tables+implicit_figures+pipe_tables",
        outputfile=str(OUT),
        extra_args=[
            f"--resource-path={DOCS}",
            "--toc",
            "--toc-depth=2",
            f"--metadata=title:{config['site_name']}",
            f"--metadata=subtitle:{config.get('extra', {}).get('version', '')}",
        ],
    )
    print(f"DOCX: {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
