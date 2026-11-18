# pystage.org

Source of the PyStage website, https://www.pystage.org. It is plain static HTML and CSS: no build step, no framework, no JavaScript, and no third-party requests (no CDNs, fonts or trackers).

## Structure

- `index.html`, `getting-started.html`, `convert.html`, `community.html`: the pages. Header and footer are duplicated in each file, so change them in all pages.
- `404.html`: error page. It uses root-absolute URLs because GitHub Pages serves it from any path.
- `style.css`: the only stylesheet. Colors are variables at the top; dark mode follows `prefers-color-scheme`.
- `assets/`: logo, banner, demo GIF and video thumbnail. `favicon.png` is the logo.
- `CNAME`: custom domain, keep unchanged. `.nojekyll`: tells GitHub Pages not to run Jekyll.

Code examples come from the README of https://github.com/pystage/pystage. Keep them identical to it. The syntax colors are hand-written `<span class="k|s|c|f">` elements.

## Preview

```
python -m http.server 8000
```

Then open http://localhost:8000.

## Publishing and reviews

The site is served from the branch `pages`, which `tools/publish-pages.sh` rebuilds from scratch on every run: the root is `main`, and every branch named `review/<name>` appears under `review/<name>/` (further slashes in the name become dashes). Nothing else is published. `review/index.html` lists all current reviews. A GitHub Action (`.github/workflows/publish-pages.yml`) runs the script with `--push` on every push to `main` or `review/**`, when a branch is deleted, and on manual start. Locally, `tools/publish-pages.sh [--dry-run] [--push]` commits to the local `pages` branch and pushes only with `--push`.

Start a review (new language, new teaching material, any change that needs feedback first):

1. Create the branch from an up-to-date `main`: `git switch -c review/<name> main`. It must contain `.github/workflows/publish-pages.yml`; if it does not, the maintainer starts the workflow by hand (Actions, Publish pages, Run workflow).
2. Add `REVIEW.md` at the root: first line `# <title>`, a line `Issue: <url of the GitHub issue>`, then a short description (the first paragraph is shown in the list). Without it the branch name is the title.
3. Push. After a minute or two the review is at https://www.pystage.org/review/<name>/.

Review copies carry a banner on every page with the title, the issue link and the official site, and `noindex` for search engines. `REVIEW.md` and `CNAME` are not published, and root-absolute links such as those in `404.html` are rewritten to the review directory. Nothing else is changed.

A review ends by merging the branch into `main` (delete `REVIEW.md` first) and deleting the branch; its directory disappears on the next run.

One-time setting for the maintainer: Settings, Pages, Source "Deploy from a branch", Branch `pages`, folder `/ (root)`. The custom domain stays www.pystage.org (its `CNAME` comes from `main`). `main` itself is no longer deployed directly; the pages branch is what is live.
