#!/usr/bin/env python3
from pathlib import Path
import json, shutil, sys
ROOT=Path(__file__).resolve().parents[1]

def load_problems():
    rows=[]
    for path in sorted((ROOT / "days").glob("day-*/problems.json")):
        rows.extend(json.loads(path.read_text(encoding="utf-8")))
    return rows

if len(sys.argv)!=2:
    print("Usage: python curriculum/scripts/new_solution.py <BOJ problem id>"); sys.exit(1)
pid=sys.argv[1]
p=next((x for x in load_problems() if x["platform"]=="BOJ" and x["problem_id"]==pid),None)
if not p:
    print(f"Problem {pid} not found in Day 1-30 DB"); sys.exit(1)
target=ROOT/'solutions'/'boj'/pid
if target.exists(): print(f"Already exists: {target}"); sys.exit(0)
template=ROOT/'solutions'/'_template'; target.mkdir(parents=True)
for src in template.iterdir():
    if src.is_file():
        text=src.read_text(encoding='utf-8').replace('{{PROBLEM_ID}}',pid).replace('{{TITLE}}',p['title'] or f'BOJ {pid}')
        (target/src.name).write_text(text,encoding='utf-8')
print(f"Created: {target}")
print(f"Day {p['day']:02d} / Grade {p['grade']} / {p['primary_topic']}")
