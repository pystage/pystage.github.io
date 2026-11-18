#!/usr/bin/env bash
#
# publish-pages.sh - build the pages branch: the website plus all review versions.
#
# The root of the pages branch is main (the official website, with its CNAME).
# Every branch named review/<name> is published under review/<name>/:
#
#   https://www.pystage.org/
#   https://www.pystage.org/review/lithuanian/
#
# Nothing else is published: no tags, no other branches. Further slashes in
# <name> become dashes. review/index.html lists the current reviews.
#
# A review branch may carry a file REVIEW.md in its root:
#
#   # Title of the review
#   Issue: https://github.com/pystage/pystage/issues/123
#
#   First paragraph: short description, shown in the list.
#
# Without it the branch name is the title. REVIEW.md is not published.
#
# Every review copy is changed in three ways, and in no other:
#   - REVIEW.md and CNAME are removed (the domain belongs to main only),
#   - every HTML page gets <meta name="robots" content="noindex"> and a banner
#     at the top of <body> naming the review, its issue and the official site,
#   - root-absolute links (href="/..", src="/..", as used by 404.html) are
#     rewritten to the review directory, since they would leave it otherwise.
#
# The pages branch is rebuilt from the refs on every run, so a deleted review
# branch loses its directory. Commits, but pushes only with --push.
#
# usage:
#   tools/publish-pages.sh [options]
#
# options:
#   --remote NAME     remote to read and push (default origin)
#   --branch NAME     branch to publish into (default pages)
#   --root REF        branch served at the root (default main)
#   --push            push the pages branch when it changed
#   --dry-run         show what would be published, change nothing
#
# .nojekyll is always written (no Jekyll processing on GitHub Pages).
#
set -euo pipefail

remote=origin
pages_branch=pages
root_ref=main
push=no
dry=no
prefix=review

while [ $# -gt 0 ]; do
    case "$1" in
        --remote) remote=$2; shift 2 ;;
        --branch) pages_branch=$2; shift 2 ;;
        --root)   root_ref=$2; shift 2 ;;
        --push)   push=yes; shift ;;
        --dry-run) dry=yes; push=no; shift ;;
        -h|--help) sed -n '2,44p' "$0" | sed 's/^# \?//'; exit 0 ;;
        *) echo "unknown option $1" >&2; exit 1 ;;
    esac
done

cd "$(git rev-parse --show-toplevel)"

echo "fetching $remote"
git fetch --quiet --prune "$remote"

root="refs/remotes/$remote/$root_ref"
if ! git rev-parse --verify --quiet "$root" >/dev/null; then
    echo "$remote/$root_ref does not exist" >&2
    exit 1
fi

if git ls-tree --name-only "$root" | grep -qx "$prefix"; then
    echo "$remote/$root_ref already has a $prefix entry; it is reserved for the reviews" >&2
    exit 1
fi

# review branches: "<ref> <directory>"
reviews=()
while read -r branch; do
    case "$branch" in
        "$prefix"/?*) ;;
        *) continue ;;
    esac
    name=${branch#"$prefix"/}
    reviews+=("refs/remotes/$remote/$branch ${name//\//-} $branch")
done < <(git for-each-ref --format='%(refname:strip=3)' "refs/remotes/$remote" | sort)

echo "root: $remote/$root_ref"
for entry in ${reviews+"${reviews[@]}"}; do
    read -r ref dir _ <<<"$entry"
    echo "  $prefix/$dir  <- $ref"
done

[ "$dry" = yes ] && { echo "dry run, nothing written"; exit 0; }

build=$(mktemp -d)
worktree=$(mktemp -d)
trap 'rm -rf "$build"; git worktree remove --force "$worktree" 2>/dev/null || true; rm -rf "$worktree"' EXIT

escape() { sed -e 's/&/\&amp;/g' -e 's/</\&lt;/g' -e 's/>/\&gt;/g' -e 's/"/\&quot;/g'; }

# the site as it will be served
git archive "$root" | tar -x -C "$build"
mkdir -p "$build/$prefix"

items=""
for entry in ${reviews+"${reviews[@]}"}; do
    read -r ref dir branch <<<"$entry"
    dest="$build/$prefix/$dir"
    mkdir -p "$dest"
    git archive "$ref" | tar -x -C "$dest"

    # metadata from REVIEW.md
    title=$branch
    issue=
    desc=
    if git cat-file -e "$ref:REVIEW.md" 2>/dev/null; then
        meta=$(git show "$ref:REVIEW.md" | tr -d '\r')
        first=$(printf '%s\n' "$meta" | head -n 1)
        case "$first" in
            "# "*) title=${first#"# "} ;;
        esac
        issue=$(printf '%s\n' "$meta" | sed -n 's/^Issue:[[:space:]]*//p' | head -n 1)
        # first paragraph that is neither the heading nor an Issue line
        desc=$(printf '%s\n' "$meta" | tail -n +2 | grep -v '^Issue:' | awk '
            NF { found=1; printf "%s%s", (n++ ? " " : ""), $0; next }
            found { exit }')
    fi
    case "$issue" in
        https://*|http://*) ;;
        *) issue= ;;
    esac
    date=$(git log -1 --format=%cs "$ref")

    rm -f "$dest/REVIEW.md" "$dest/CNAME"

    # banner, noindex, and root-absolute links, in every HTML page
    base="/$prefix/$dir/"
    banner="<div class=\"review-banner\" style=\"background:#ffd54a;color:#000;padding:.6rem 1rem;text-align:center;font:600 15px/1.4 sans-serif;border-bottom:2px solid #b8860b\">Review version: $(printf '%s' "$title" | escape) &mdash; not the official website."
    if [ -n "$issue" ]; then
        banner="$banner Feedback: <a href=\"$(printf '%s' "$issue" | escape)\" style=\"color:#000\">$(printf '%s' "$issue" | escape)</a>."
    fi
    banner="$banner Official site: <a href=\"https://www.pystage.org/\" style=\"color:#000\">https://www.pystage.org/</a></div>"
    # shellcheck disable=SC2016  # perl code, not shell
    find "$dest" -type f \( -name '*.html' -o -name '*.htm' \) -print0 |
        BANNER=$banner BASE=$base xargs -0 perl -0pi -e '
            s{(\b(?:href|src)=")/(?!/)}{$1$ENV{BASE}}g;
            s{(</head>)}{<meta name="robots" content="noindex">\n$1}i;
            s{(<body[^>]*>)}{$1\n$ENV{BANNER}}i;'

    item="<li><h2><a href=\"$dir/\">$(printf '%s' "$title" | escape)</a></h2>"
    [ -n "$desc" ] && item="$item<p>$(printf '%s' "$desc" | escape)</p>"
    item="$item<p class=\"meta\"><a href=\"$dir/\">Review site</a>"
    [ -n "$issue" ] && item="$item &middot; <a href=\"$(printf '%s' "$issue" | escape)\">GitHub issue</a>"
    item="$item &middot; branch <code>$(printf '%s' "$branch" | escape)</code> &middot; last commit $date</p></li>"
    items="$items$item"$'\n'
done

{
    cat <<'HTML'
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>Reviews | PyStage</title>
<meta name="color-scheme" content="light dark">
<link rel="icon" type="image/png" href="../favicon.png">
<link rel="stylesheet" href="../style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site"><div class="wrap">
<a class="brand" href="../index.html"><img src="../assets/logo.png" alt="" width="40" height="40">PyStage</a>
<nav aria-label="Main"><ul><li><a href="../index.html">Home</a></li><li><a href="../getting-started.html">Getting started</a></li><li><a href="../convert.html">Convert Scratch</a></li><li><a href="../community.html">Community</a></li><li><a href="../docs.html">Docs</a></li></ul></nav>
</div></header>
<main id="main"><div class="wrap">
<h1>Reviews</h1>
<p class="lead">Versions of the website that are being reviewed. They are not the official website and are not indexed by search engines.</p>
HTML
    if [ -n "$items" ]; then
        printf '<ul>\n%s</ul>\n' "$items"
    else
        echo "<p>No reviews at the moment.</p>"
    fi
    cat <<'HTML'
</div></main>
</body>
</html>
HTML
} > "$build/$prefix/index.html"

touch "$build/.nojekyll"

# check out the pages branch beside the working copy; it may exist on the
# remote, only locally, or not at all
if git rev-parse --verify --quiet "refs/remotes/$remote/$pages_branch" >/dev/null; then
    base_ref="refs/remotes/$remote/$pages_branch"
elif git rev-parse --verify --quiet "refs/heads/$pages_branch" >/dev/null; then
    echo "$pages_branch is not on $remote, continuing from the local branch"
    base_ref="refs/heads/$pages_branch"
else
    base_ref=""
fi

checked_out=$(git worktree list --porcelain | awk -v b="refs/heads/$pages_branch" '
    /^worktree /{ path=$2 } $0 == "branch " b { print path }')
if [ -n "$checked_out" ]; then
    echo "$pages_branch is checked out in $checked_out; switch that worktree to another branch" >&2
    exit 1
fi

if [ -n "$base_ref" ]; then
    git worktree add --quiet --force -B "$pages_branch" "$worktree" "$base_ref"
else
    echo "creating $pages_branch"
    git worktree add --quiet --force --detach "$worktree"
    git -C "$worktree" checkout --quiet --orphan "$pages_branch"
    git -C "$worktree" rm --quiet -rf . 2>/dev/null || true
fi

# replace the contents wholesale, so deleted reviews take their directory
find "$worktree" -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} +
cp -a "$build/." "$worktree/"

git -C "$worktree" add --all
if git -C "$worktree" diff --cached --quiet; then
    echo "nothing changed"
    exit 0
fi

git -C "$worktree" commit --quiet -m "Publish main $(git rev-parse --short "$root") and ${#reviews[@]} reviews"
echo "committed $(git -C "$worktree" rev-parse --short HEAD) on $pages_branch"

if [ "$push" = yes ]; then
    git -C "$worktree" push --quiet "$remote" "$pages_branch"
    echo "pushed to $remote/$pages_branch"
else
    echo "not pushed"
fi
