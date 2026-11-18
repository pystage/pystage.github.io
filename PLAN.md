# Website plan

This document describes what www.pystage.org contains, for whom, in which languages, and how the
translations are kept in sync. It is the reference for changes to the website.

## Audiences

| Audience | Languages | Where |
|---|---|---|
| **Kids** | every language PyStage supports (required) | website |
| **Teachers** | every language for the core page; deeper material may be English only, marked "(English)" | website |
| **Developers** | English only | README, CONTRIBUTING.md, TRANSLATING.md, Read the Docs, one English "Developers" page on the website |

**English is always the authoritative source.** Every other language is a translation of the
English pages and is updated after them.

## Pages

The page structure is the same in every language. English lives at the root, other languages under
`/<lang>/` (e.g. `/de/`).

### For kids

1. **Home** – what you can do with PyStage, a demo, one big "Start here" button, a smaller link for
   teachers. The language switcher is visible at the top, so a child who lands on the English page
   finds its language.
2. **Start** – install Python and PyStage, the first program, step by step, in simple words.
3. **Blocks** – one section per Scratch category (Motion, Looks, Sound, Events, Control, Sensing,
   Operators, Variables, Pen): the block as a picture in the kid's language (rendered by
   scratchblocks) next to the Python method. **Generated** from the docstrings of the language's
   facade (`pystage.en`, `pystage.de`, …), which already contain a `Scratch block:` line, so the
   reference is translated with the API and never outdated. It replaces Read the Docs as the
   reference for kids; Read the Docs stays the technical reference.
4. **Convert** – turn your own Scratch project into Python with the web converter.
5. **Projects** – small step-by-step projects. Starts with one; more later (issues #5, #21).

### For teachers

6. **For teachers** (translated) – what PyStage is and how it bridges Scratch and Python; how code
   behaves like Scratch (scripts, loops refresh the screen, functions are custom blocks, no-refresh
   mode, errors); setting it up in class (installation on school computers, editors); the converter
   including the command line and privacy (uploads are deleted after 7 days); what is not supported;
   choosing a language for a class (dropdown values and messages follow the API language).
7. **Material** – lesson ideas, worksheets, background. May stay English only; other languages link
   to the English page and mark it "(English)".

### English only

8. **Developers** – links to README, CONTRIBUTING.md, TRANSLATING.md, Read the Docs (core, converter,
   l10n), how to add a language, contributors, maintainer, licence. Other languages link to it,
   marked "(English)".

### All languages

9. **Contact** – Discord and GitHub, short.

## Keeping translations in sync

- Every translated page records the English page it was translated from: front matter
  `translation_of: <path>` and `source_hash: <hash of the English source file>`.
  `tools/check-translations.py` lists translated pages whose English source changed since; run it
  before a release or in CI.
- A page that is not translated yet appears in the menu of that language as a link to the English
  page, marked "(English)".
- A language that has not been reviewed by a native speaker shows a short note on every page
  ("machine-assisted translation, help us improve it").
- Reviews of new languages or new material happen on `review/<name>` branches, which are published
  under `/review/<name>/` (see README, "Publishing and reviews").

## Technology

- [Hugo](https://gohugo.io/) as static site generator, with a small custom theme in the repository
  (no external theme), based on the look of the previous hand-written site (light and dark mode,
  works at phone width, accessible).
- Multilingual setup of Hugo: English at the root, other languages in subdirectories; UI strings in
  `i18n/<lang>.toml`; content in `content/<lang>/`.
- Block data: `tools/extract-blocks.py` reads the installed pystage facades and writes
  `data/blocks/<lang>.json`; the Blocks pages are rendered from these files. The data files are
  committed, so building the site needs Hugo only, no Python.
- Code examples on the pages must run; `tools/check-examples.py` extracts and runs them headless.
- Publishing: `tools/publish-pages.sh` builds every published ref (main at the root, review branches
  under `/review/<name>/`) with Hugo when the ref contains a Hugo configuration, and copies plain
  files otherwise.

## Order of work

1. English pages restructured by audience; developer content moved out. Hugo, theme, plan.
2. Generated Blocks pages (all languages at once).
3. German kids' pages and teacher page.
4. Lithuanian kids' pages and teacher page (after the review of the Lithuanian API, issue #133).
5. Projects and teacher material, English first.
