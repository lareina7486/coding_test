#!/usr/bin/env python3
from pathlib import Path
from collections import Counter
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
problems = json.loads((ROOT / "db" / "problem-index.json").read_text(encoding="utf-8"))
days = json.loads((ROOT / "db" / "days.json").read_text(encoding="utf-8"))

errors = []

if len(days) != 30:
    errors.append(f"Day count: expected 30, got {len(days)}")

keys = [p["key"] for p in problems]
if len(keys) != len(set(keys)):
    errors.append("Duplicate problem keys found")

grade_counts = Counter(p["grade"] for p in problems)
if grade_counts != Counter({"S": 65, "A": 308}):
    errors.append(f"Grade counts mismatch: {dict(grade_counts)}")

if len(problems) != 373:
    errors.append(f"Problem count: expected 373, got {len(problems)}")

for d in days:
    day = d["day"]
    readme = ROOT / d["path"]
    yaml_file = ROOT / "days" / f"day-{day:02d}" / "problems.yaml"
    if not readme.exists():
        errors.append(f"Missing {readme}")
    if not yaml_file.exists():
        errors.append(f"Missing {yaml_file}")

if errors:
    print("VALIDATION FAILED")
    for e in errors:
        print("-", e)
    sys.exit(1)

print("OK")
print(f"Days: {len(days)}")
print(f"Problems: {len(problems)}")
print(f"S: {grade_counts['S']} / A: {grade_counts['A']}")
