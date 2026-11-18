#!/usr/bin/env python3
"""Run the runnable Python examples of the site headless.

An example is runnable when its code fence is marked with {run=true}:

    ```python {run=true}
    ...
    ```

Hugo ignores the unknown option, so it does not show on the page. Unmarked fences (install
commands, fragments) are not run. The script scans content/<lang>/**/*.md for all languages.

Each example is written to a temporary file (PyStage needs the source of the scripts) and run with
SDL_VIDEODRIVER=dummy and SDL_AUDIODRIVER=dummy. The last call of the form <name>.play() (or
.abspielen(), .paleisk(); any method name given with --play-names) is replaced by 60 frames of
<name>._core._frame(1/30).

Usage: tools/check-examples.py [--python PYTHON] [--timeout SECONDS] [--list] [--play-names a,b] [PATH ...]
Exit status 1 if an example fails. Only the standard library is used.
"""
import argparse, os, re, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FENCE = re.compile(r"^(\s*)(`{3,}|~{3,})\s*python\b([^\n]*)$")
DEFAULT_PLAY = "play,abspielen,paleisk"


def examples(path):
    """Yield (line number, code) of each runnable python fence in a Markdown file."""
    lines = path.read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(lines):
        m = FENCE.match(lines[i])
        if m and re.search(r"\brun\s*=\s*(true|\"true\")", m.group(3)):
            indent, fence = m.group(1), m.group(2)
            start, code = i + 1, []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith(fence):
                code.append(lines[i][len(indent):] if lines[i].startswith(indent) else lines[i])
                i += 1
            yield start, "\n".join(code) + "\n"
        i += 1


def prepare(code, play_names, frames=60):
    pattern = re.compile(r"^(\s*)(\w+)\.(%s)\(\)\s*$" % "|".join(map(re.escape, play_names)), re.M)
    matches = list(pattern.finditer(code))
    if not matches:
        return None
    m = matches[-1]
    repl = "%sfor _ in range(%d):\n%s    %s._core._frame(1 / 30)" % (m.group(1), frames, m.group(1), m.group(2))
    return code[:m.start()] + repl + code[m.end():]


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("paths", nargs="*", help="Markdown files or directories (default: content/)")
    ap.add_argument("--python", default="python", help="Python interpreter with pystage installed")
    ap.add_argument("--timeout", type=int, default=60)
    ap.add_argument("--play-names", default=DEFAULT_PLAY)
    ap.add_argument("--list", action="store_true", help="only list the examples")
    args = ap.parse_args()
    play_names = [n for n in args.play_names.split(",") if n]
    files = []
    for p in args.paths or [ROOT / "content"]:
        p = Path(p)
        files += sorted(p.rglob("*.md")) if p.is_dir() else [p]
    env = dict(os.environ, SDL_VIDEODRIVER="dummy", SDL_AUDIODRIVER="dummy", PYGAME_HIDE_SUPPORT_PROMPT="1")
    total = failed = 0
    with tempfile.TemporaryDirectory() as tmp:
        for f in files:
            for line, code in examples(f):
                total += 1
                label = "%s:%d" % (f.relative_to(ROOT) if f.is_relative_to(ROOT) else f, line)
                if args.list:
                    print(label)
                    continue
                prepared = prepare(code, play_names)
                if prepared is None:
                    failed += 1
                    print("FAIL %s: no final .play() call found" % label)
                    continue
                script = Path(tmp) / ("example_%d.py" % total)
                script.write_text(prepared, encoding="utf-8")
                try:
                    r = subprocess.run([args.python, str(script)], env=env, cwd=tmp, capture_output=True,
                                       text=True, timeout=args.timeout)
                    out = (r.stdout + r.stderr).strip()
                    if r.returncode != 0 or "Traceback" in out:
                        failed += 1
                        print("FAIL %s\n%s" % (label, out))
                    else:
                        print("ok   %s" % label)
                except subprocess.TimeoutExpired:
                    failed += 1
                    print("FAIL %s: timeout" % label)
    print("%d examples, %d failed" % (total, failed))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
