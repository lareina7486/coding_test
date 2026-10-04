#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[1]

def load_problems():
    rows=[]
    for path in sorted((ROOT / "days").glob("day-*/problems.json")):
        rows.extend(json.loads(path.read_text(encoding="utf-8")))
    return rows

if len(sys.argv)!=2:
    print("Usage: python curriculum/scripts/new_submission.py <BOJ problem id>"); sys.exit(1)
pid=sys.argv[1]
p=next((x for x in load_problems() if x["platform"]=="BOJ" and x["problem_id"]==pid),None)
if not p: print(f"Problem {pid} not found"); sys.exit(1)
target=ROOT/'submissions'/f"day-{p['day']:02d}"/f"boj-{pid}"; target.mkdir(parents=True,exist_ok=True)
num=len(list(target.glob('attempt-*.py')))+1
attempt=target/f"attempt-{num:02d}.py"
attempt.write_text(f"# BOJ {pid} — {p['title'] or ''}\n# Day {p['day']:02d} / Grade {p['grade']} / {p['primary_topic']}\n\n# TODO: 내 풀이\n",encoding='utf-8')
print(f"Created: {attempt}")
