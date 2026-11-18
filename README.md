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

## Publishing

GitHub Pages deploys from branch `main`, folder `/` (root). Push to `main` to publish.
