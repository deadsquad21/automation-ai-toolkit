#!/usr/bin/env python3
"""Provider-neutral local workflow runner.

The toolkit intentionally ships without embedded API keys or vendor credentials.
"""
import argparse, json, pathlib, re

def step_replace(text, cfg):
    return text.replace(cfg.get("old",""), cfg.get("new",""))

def step_regex(text, cfg):
    return re.sub(cfg["pattern"], cfg.get("replacement",""), text)

def step_prefix(text, cfg):
    return cfg.get("text","") + text

def step_suffix(text, cfg):
    return text + cfg.get("text","")

STEPS = {
    "replace": step_replace,
    "regex": step_regex,
    "prefix": step_prefix,
    "suffix": step_suffix,
}

def run(text, workflow):
    for item in workflow:
        kind = item["type"]
        if kind not in STEPS:
            raise ValueError(f"Unsupported step: {kind}")
        text = STEPS[kind](text, item)
    return text

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("workflow")
    ap.add_argument("input")
    ap.add_argument("--output")
    args = ap.parse_args()
    wf = json.loads(pathlib.Path(args.workflow).read_text(encoding="utf-8"))
    text = pathlib.Path(args.input).read_text(encoding="utf-8")
    result = run(text, wf["steps"])
    if args.output:
        pathlib.Path(args.output).write_text(result, encoding="utf-8")
    else:
        print(result)

if __name__ == "__main__":
    main()
