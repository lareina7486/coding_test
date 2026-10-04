#!/usr/bin/env python3
from pathlib import Path
from collections import Counter
import json, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
problems=[]
for day in range(1,31):
    day_dir=ROOT/'days'/f'day-{day:02d}'
    readme=day_dir/'README.md'
    data=day_dir/'problems.json'
    if not readme.exists(): errors.append(f"Missing {readme}")
    if not data.exists():
        errors.append(f"Missing {data}")
        continue
    rows=json.loads(data.read_text(encoding="utf-8"))
    for p in rows:
        if p.get("day") != day: errors.append(f"Day mismatch: {p.get('key')} -> {p.get('day')} in day-{day:02d}")
    problems.extend(rows)
keys=[p["key"] for p in problems]
if len(keys)!=len(set(keys)): errors.append("Duplicate problem keys found")
grades=Counter(p["grade"] for p in problems)
if len(problems)!=373: errors.append(f"Problem count expected 373, got {len(problems)}")
if grades != Counter({"S":65,"A":308}): errors.append(f"Grade counts mismatch: {dict(grades)}")
if errors:
    print("VALIDATION FAILED")
    for e in errors: print("-",e)
    sys.exit(1)
print("OK")
print(f"Days: 30 / Problems: {len(problems)} / S: {grades['S']} / A: {grades['A']}")
