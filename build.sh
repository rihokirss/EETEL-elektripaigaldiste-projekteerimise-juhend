#!/usr/bin/env bash
# Build the full site: HTML + PDF + DOCX.
#
# Usage:
#   ./build.sh           # HTML + PDF + DOCX
#   ./build.sh --no-pdf  # HTML only (fast)
#   ./build.sh --no-docx # HTML + PDF (skip DOCX)

set -euo pipefail

cd "$(dirname "$0")"

# shellcheck disable=SC1091
source .venv/bin/activate

WANT_PDF=1
WANT_DOCX=1
for arg in "$@"; do
    case "$arg" in
        --no-pdf)  WANT_PDF=0; WANT_DOCX=0 ;;
        --no-docx) WANT_DOCX=0 ;;
        *) echo "unknown arg: $arg" >&2; exit 2 ;;
    esac
done

if [[ $WANT_PDF -eq 1 ]]; then
    echo "==> mkdocs build (HTML + PDF)"
    ENABLE_PDF_EXPORT=1 mkdocs build
else
    echo "==> mkdocs build (HTML only)"
    mkdocs build
fi

if [[ $WANT_DOCX -eq 1 ]]; then
    echo "==> build-docx.py (DOCX)"
    python build-docx.py
fi

echo "==> done"
ls -la site/pdf/ 2>/dev/null || true
