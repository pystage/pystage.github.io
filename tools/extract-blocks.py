#!/usr/bin/env python3
"""Extract the block reference of the pystage language facades into data/blocks/<lang>.json.

Usage: extract-blocks.py <lang> [<lang> ...]      (run with the Python that has pystage installed)

For every public method of the sprite and stage class of pystage.<lang> the script finds the core
method it delegates to (the same bytecode lookup as pystage.l10n.api), takes the category from the
core method prefix and the order from the position of the core method in the source, and parses the
numpy-style docstring: summary, further paragraphs, the "Scratch block:" line (scratchblocks syntax)
and the parameters. Methods of sprite and stage that call the same core method are merged into one entry.
"""
import dis
import importlib
import inspect
import json
import re
import sys
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data" / "blocks"

CATEGORIES = [  # (id, core prefixes)
    ("motion", ("motion_",)),
    ("looks", ("looks_",)),
    ("sound", ("sound_",)),
    ("events", ("event_",)),
    ("control", ("control_",)),
    ("sensing", ("sensing_",)),
    ("operators", ("operator_",)),
    ("variables", ("data_",)),
    ("pen", ("pen_",)),
    ("extras", ("pystage_", "sprite_", "")),
]
BLOCK_LINE = re.compile(r"^Scratch(?: block|-Block| blokas):\s*(.*\S)\s*$")


def category_of(core):
    if core is None:
        return "extras"
    for cat, prefixes in CATEGORIES:
        if any(p and core.startswith(p) for p in prefixes):
            return cat
    return "extras"


def core_name(func):
    """Name of the core method a facade method delegates to, or None."""
    for ins in dis.Bytecode(func):
        if ins.opname in ("LOAD_METHOD", "LOAD_ATTR") and ins.argval != "_core":
            # only count attributes of self._core
            return ins.argval
    return None


def parse_doc(doc):
    doc = inspect.cleandoc(doc or "")
    sections = r"\n(?:Returns|Raises|Yields|See Also|Notes|Examples)\n-{3,}"
    head, _, params_text = doc.partition("\nParameters\n----------")
    head = re.split(sections, head)[0]
    params_text = re.split(sections, params_text)[0]
    block = None
    paras = []
    for para in re.split(r"\n\s*\n", head):
        lines = para.strip().splitlines()
        if lines and BLOCK_LINE.match(lines[0].strip()):
            block = BLOCK_LINE.match(lines[0].strip()).group(1)
            continue
        if para.strip():
            paras.append(" ".join(l.strip() for l in lines))
    params = {}
    cur = None
    for line in params_text.splitlines():
        m = re.match(r"^(\*{0,2}\w+)\s*:\s*(.*)$", line)
        if m:
            cur = m.group(1)
            params[cur] = {"type": m.group(2).strip(), "description": ""}
        elif cur and line.strip():
            d = params[cur]["description"]
            params[cur]["description"] = (d + " " + line.strip()).strip()
    return {
        "summary": paras[0] if paras else "",
        "more": paras[1:],
        "block": block,
        "params": params,
    }


def describe(name, func):
    sig = inspect.signature(func)
    parsed = parse_doc(func.__doc__)
    params = []
    for p in sig.parameters.values():
        if p.name == "self":
            continue
        info = parsed["params"].get(p.name, {})
        params.append({
            "name": p.name,
            "type": info.get("type", ""),
            "default": None if p.default is inspect.Parameter.empty else repr(p.default),
            "description": info.get("description", ""),
        })
    return {
        "name": name,
        "params": params,
        "summary": parsed["summary"],
        "more": parsed["more"],
        "block": parsed["block"],
    }


def extract(lang):
    from pystage.core.sprite import CoreSprite
    from pystage.core.stage import CoreStage
    mod = importlib.import_module(f"pystage.{lang}")
    classes = {"sprite": (mod.sprite_class, CoreSprite), "stage": (mod.stage_class, CoreStage)}
    entries = {}
    for kind, (cls, corecls) in classes.items():
        for name, func in inspect.getmembers(cls, predicate=inspect.isfunction):
            if name.startswith("_"):
                continue
            core = core_name(func)
            if core is not None and not hasattr(corecls, core):
                core = None
            key = core or f"{kind}.{name}"
            d = describe(name, func)
            e = entries.setdefault(key, {"core": core, "category": category_of(core), "for": {}})
            e["for"][kind] = d
            if core:
                try:
                    e["_pos"] = inspect.getsourcelines(getattr(corecls, core))[1]
                except (OSError, TypeError):
                    e["_pos"] = 10 ** 6
            else:
                e["_pos"] = 10 ** 6
    order = [c for c, _ in CATEGORIES]
    result = []
    for key, e in entries.items():
        main = e["for"].get("sprite") or e["for"].get("stage")
        result.append({
            "core": e["core"],
            "category": e["category"],
            "available": [k for k in ("sprite", "stage") if k in e["for"]],
            "names": {k: v["name"] for k, v in e["for"].items()},
            "summary": main["summary"],
            "more": main["more"],
            "block": main["block"],
            "params": main["params"],
            "_sort": (order.index(e["category"]), e["_pos"], e["core"] or main["name"]),
        })
    result.sort(key=lambda r: r["_sort"])
    for r in result:
        del r["_sort"]
    variables = {k: cls.__name__ for k, (cls, _) in classes.items()}
    return {"language": lang, "classes": variables, "blocks": result}


def main(langs):
    DATA.mkdir(parents=True, exist_ok=True)
    for lang in langs:
        data = extract(lang)
        (DATA / f"{lang}.json").write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        n = len(data["blocks"])
        print(f"{lang}: {n} entries, {sum(1 for b in data['blocks'] if not b['block'])} without block line")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:])
