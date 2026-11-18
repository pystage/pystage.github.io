# pystage.org

Source of the PyStage website, https://www.pystage.org. It is built with [Hugo](https://gohugo.io/) (extended, v0.157 or newer) from a small custom theme in `layouts/`. No JavaScript, no third-party requests (no CDNs, fonts or trackers). The plan (audiences, pages, translations) is in `PLAN.md`.

## Structure

- `hugo.toml`: languages (`en` at the root, `de` under `/de/`), markup and site parameters. `[languages.<lang>.params] reviewed = false` shows the "not reviewed by a native speaker" note on every page of that language.
- `content/<lang>/`: the pages (Markdown). Front matter: `title`, `menu_title`, `description`, `lead`, and for the menu `nav: kids|teachers|developers|all` plus `weight`. Pages without `nav` are not in the menu.
- `i18n/<lang>.toml`: all UI strings. A new language needs this file and `content/<lang>/` (a language without them is set `disabled = true` in `hugo.toml`).
- `layouts/`: the theme. The menu is generated from the `nav` pages of the English site; in another language each entry links to the translated page, or to the English page marked "(English)" when there is none. The language switcher in the header lists the enabled languages and links to the same page, or to the language's home. `layouts/blocks/list.html` is the hook for the generated Blocks pages (`data/blocks/<lang>.json`).
- `assets/css/style.css`: the only stylesheet (colors are variables at the top; dark mode follows `prefers-color-scheme`).
- `static/`: copied to the output root: `assets/` (logo, banner, demo GIF), `favicon.png`, `CNAME`, `.nojekyll`.
- `tools/check-examples.py`: runs the code examples marked ```` ```python {run=true} ```` headless (`--python` selects the interpreter that has pystage).
- `tools/check-translations.py`: lists outdated and missing translations (`translation_of`, `source_hash` in the front matter of translated pages; `--hash start.md` prints the hash of an English page).

Inside Markdown use root-absolute links (`[Start](/start/)`, `/assets/x.png`); they are prefixed with the language and the base URL, so they work under `/review/<name>/` too. In raw HTML use the shortcodes `{{< rl "/start/" >}}` (page link; `<a {{< rla "/start/" >}}>` also writes the `href` itself) and `{{< asset "/assets/x.png" >}}`.

## Preview

```
hugo server
```

or `hugo --minify` and `python -m http.server` in `public/`. To test a non-root location: `hugo --minify --baseURL http://localhost:8000/review/new-website/`.

## Publishing and reviews

The site is served from the branch `pages`, which `tools/publish-pages.sh` rebuilds from scratch on every run: the root is `main`, and every branch named `review/<name>` appears under `review/<name>/` (further slashes in the name become dashes). Nothing else is published. `review/index.html` lists all current reviews. A GitHub Action (`.github/workflows/publish-pages.yml`) runs the script with `--push` on every push to `main` or `review/**`, when a branch is deleted, and on manual start. Locally, `tools/publish-pages.sh [--dry-run] [--push]` commits to the local `pages` branch and pushes only with `--push`.

Start a review (new language, new teaching material, any change that needs feedback first):

1. Create the branch from an up-to-date `main`: `git switch -c review/<name> main`. It must contain `.github/workflows/publish-pages.yml`; if it does not, the maintainer starts the workflow by hand (Actions, Publish pages, Run workflow).
2. Add `REVIEW.md` at the root: first line `# <title>`, a line `Issue: <url of the GitHub issue>`, then a short description (the first paragraph is shown in the list). Without it the branch name is the title.
3. Push. After a minute or two the review is at https://www.pystage.org/review/<name>/.

Review copies carry a banner on every page with the title, the issue link and the official site, and `noindex` for search engines. `REVIEW.md` and `CNAME` are not published, and root-absolute links such as those in `404.html` are rewritten to the review directory. Nothing else is changed.

Hugo: if the root of `main` or of a review branch holds a Hugo configuration (`hugo.toml`, `config.toml`, ..., `config/_default/`), the script builds it with `hugo --minify --baseURL <its public URL>` and publishes the output instead of the raw tree, so a review can be a Hugo site (themes must be inside the branch, git submodules are not fetched). The banner and `noindex` are added to the built pages; a `CNAME` at the root of a Hugo `main` is copied into the output. If a build fails the whole run fails and nothing is published. The workflow installs Hugo extended v0.157.0 (version and checksum in the workflow file); locally `hugo` must be on the PATH, and `--base-url` changes the public root URL (default https://www.pystage.org/), e.g. for testing.

A review ends by merging the branch into `main` (delete `REVIEW.md` first) and deleting the branch; its directory disappears on the next run.

One-time setting for the maintainer: Settings, Pages, Source "Deploy from a branch", Branch `pages`, folder `/ (root)`. The custom domain stays www.pystage.org (its `CNAME` comes from `main`). `main` itself is no longer deployed directly; the pages branch is what is live.

Links to a page that has no translation (e.g. `/developers/` from a German page) go to the English page, and the link gets `lang="en"`. This is done by `layouts/partials/localize.html`, used by the link render hook and the `rl`/`rla` shortcodes.
