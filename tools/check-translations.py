#!/usr/bin/env python3
"""Report the state of the translations of the site.

English (content/en/) is the source. A translated page (content/<lang>/<path>.md) records in its
front matter

    translation_of: <path of the English page below content/en/>   (default: same path as the page)
    source_hash: <hash of the English source file when the translation was made>

The hash is the first 16 hex digits of the SHA-256 of the English file, as printed by
`tools/check-translations.py --hash <path>` (e.g. `--hash start.md`). When a translator has
updated a translation to the current English text, they set source_hash to the new value.

Output per language:
  OUTDATED   translated page whose English source changed (or has no/wrong source_hash)
  MISSING    English page without translation
  ORPHAN     translated page whose English source does not exist
Exit status 1 if anything is OUTDATED or ORPHAN (MISSING alone is not an error unless --strict).
Only the standard library is used.

Usage: tools/check-translations.py [--lang de] [--strict] [--hash PATH]
"""
import argparse, hashlib, re, sys
from pathlib import Path

CONTENT = Path(__file__).resolve().parent.parent / "content"
SOURCE = "en"


def file_hash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def front_matter(path):
    """Return the top-level scalar fields of a YAML front matter block (no dependencies)."""
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\s*\n(.*?)\n---\s*(\n|$)", text, re.S)
    fields = {}
    if m:
        for line in m.group(1).splitlines():
            k = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
            if k:
                fields[k.group(1)] = k.group(2).strip().strip("\"'")
    return fields


def pages(lang):
    base = CONTENT / lang
    return {str(p.relative_to(base)): p for p in sorted(base.rglob("*.md"))} if base.is_dir() else {}


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--lang", action="append", help="check only this language (repeatable)")
    ap.add_argument("--strict", action="store_true", help="MISSING pages are errors too")
    ap.add_argument("--hash", metavar="PATH", help="print the source hash of an English page and exit")
    args = ap.parse_args()
    if args.hash:
        print(file_hash(CONTENT / SOURCE / args.hash))
        return
    source = pages(SOURCE)
    langs = args.lang or sorted(d.name for d in CONTENT.iterdir() if d.is_dir() and d.name != SOURCE)
    problems = missing = 0
    for lang in langs:
        translated = pages(lang)
        print("== %s: %d of %d pages translated" % (lang, len(translated), len(source)))
        covered = set()
        for rel, p in translated.items():
            fm = front_matter(p)
            of = fm.get("translation_of") or rel
            src = source.get(of)
            if src is None:
                problems += 1
                print("ORPHAN   %s/%s: English source %s does not exist" % (lang, rel, of))
                continue
            covered.add(of)
            h = file_hash(src)
            if fm.get("source_hash") != h:
                problems += 1
                print("OUTDATED %s/%s: English %s is now %s (recorded: %s)" % (lang, rel, of, h, fm.get("source_hash") or "none"))
        for rel in source:
            if rel not in covered:
                missing += 1
                print("MISSING  %s/%s (linked as English page, marked \"(English)\")" % (lang, rel))
    if not langs:
        print("No translations yet (only content/%s exists)." % SOURCE)
    sys.exit(1 if problems or (args.strict and missing) else 0)


if __name__ == "__main__":
    main()
