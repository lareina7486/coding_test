# Coding Test Learning DB

100일 코딩테스트 계획 중 **Day 1~30 S/A 전범위 1회독**을 GitHub DB 형태로 만든 저장소 구조다.

## 현재 범위

- Day: **1~30**
- 고유 문제: **373개**
- S: **65개**
- A: **308개**
- 목표: 첫 30일 동안 S/A를 전부 최소 1회 노출
- 학습 방식: **S는 재현 중심 / A는 해설 고속 노출 중심**

## 학습 흐름

```text
Concept
  ↓
Pattern
  ↓
Day Problem
  ↓
내 Submission
  ↓
Judge 결과 + AI Review
  ↓
○ / △ / ×
  ↓
재풀이 Queue
  ↓
대표 Solution 정리
```

## 폴더

```text
curriculum/
├─ days/          # Day 01~30: README + problems.yaml
├─ concepts/      # 주제별 선행 개념
├─ db/            # problems / days / topics / progress JSON
├─ submissions/   # 내 시도 코드
├─ solutions/     # 대표 풀이 + 대안 풀이
├─ ai/            # AI 채점/힌트/풀이비교 프롬프트와 schema
└─ scripts/       # DB 검증, 풀이/제출 폴더 생성
```

## 하루 공부법

1. Day README를 연다.
2. `먼저 학습할 개념`을 빠르게 확인한다.
3. S는 10~15분 자력 시도 후 풀이를 보고 **닫고 재현**한다.
4. A는 3~7분 발상을 시도하고 막히면 풀이를 빠르게 본다.
5. 결과를 `○ / △ / ×`로 분류한다.
6. 직접 작성한 코드는 `submissions/`에 보존하고 AI Review를 받는다.
7. 대표 풀이가 생기면 `solutions/`에 여러 접근을 비교해 정리한다.

## Day 01~30

- [Day 01](./days/day-01/README.md) — 13문제 (S 3 / A 10)
- [Day 02](./days/day-02/README.md) — 13문제 (S 3 / A 10)
- [Day 03](./days/day-03/README.md) — 13문제 (S 3 / A 10)
- [Day 04](./days/day-04/README.md) — 13문제 (S 3 / A 10)
- [Day 05](./days/day-05/README.md) — 12문제 (S 4 / A 8)
- [Day 06](./days/day-06/README.md) — 12문제 (S 4 / A 8)
- [Day 07](./days/day-07/README.md) — 12문제 (S 0 / A 12)
- [Day 08](./days/day-08/README.md) — 12문제 (S 0 / A 12)
- [Day 09](./days/day-09/README.md) — 12문제 (S 0 / A 12)
- [Day 10](./days/day-10/README.md) — 12문제 (S 1 / A 11)
- [Day 11](./days/day-11/README.md) — 12문제 (S 1 / A 11)
- [Day 12](./days/day-12/README.md) — 13문제 (S 1 / A 12)
- [Day 13](./days/day-13/README.md) — 12문제 (S 1 / A 11)
- [Day 14](./days/day-14/README.md) — 12문제 (S 2 / A 10)
- [Day 15](./days/day-15/README.md) — 12문제 (S 2 / A 10)
- [Day 16](./days/day-16/README.md) — 12문제 (S 2 / A 10)
- [Day 17](./days/day-17/README.md) — 12문제 (S 2 / A 10)
- [Day 18](./days/day-18/README.md) — 13문제 (S 4 / A 9)
- [Day 19](./days/day-19/README.md) — 13문제 (S 4 / A 9)
- [Day 20](./days/day-20/README.md) — 13문제 (S 4 / A 9)
- [Day 21](./days/day-21/README.md) — 12문제 (S 4 / A 8)
- [Day 22](./days/day-22/README.md) — 12문제 (S 5 / A 7)
- [Day 23](./days/day-23/README.md) — 12문제 (S 5 / A 7)
- [Day 24](./days/day-24/README.md) — 14문제 (S 0 / A 14)
- [Day 25](./days/day-25/README.md) — 14문제 (S 0 / A 14)
- [Day 26](./days/day-26/README.md) — 13문제 (S 1 / A 12)
- [Day 27](./days/day-27/README.md) — 12문제 (S 1 / A 11)
- [Day 28](./days/day-28/README.md) — 12문제 (S 1 / A 11)
- [Day 29](./days/day-29/README.md) — 12문제 (S 2 / A 10)
- [Day 30](./days/day-30/README.md) — 12문제 (S 2 / A 10)

## Concept Index

- [자료구조 1 (Stack/Queue/Deque)](./concepts/data-structure-1.md)
- [자료구조 2 (Hash/Set/Heap)](./concepts/data-structure-2.md)
- [문자열](./concepts/string.md)
- [구현](./concepts/implementation.md)
- [완전탐색](./concepts/brute-force.md)
- [백트래킹](./concepts/backtracking.md)
- [투 포인터/슬라이딩 윈도우](./concepts/two-pointer-sliding-window.md)
- [누적합](./concepts/prefix-sum.md)
- [이분탐색](./concepts/binary-search.md)
- [그리디](./concepts/greedy.md)
- [그래프 탐색 (DFS/BFS)](./concepts/graph-traversal.md)
- [시뮬레이션](./concepts/simulation.md)
- [트리](./concepts/tree.md)
- [최단거리](./concepts/shortest-path.md)
- [분리 집합 (Union-Find)](./concepts/union-find.md)
- [최소 스패닝 트리 (MST)](./concepts/mst.md)
- [위상정렬](./concepts/topological-sort.md)
- [DP 1](./concepts/dp-1.md)
- [DP 2](./concepts/dp-2.md)
- [트라이](./concepts/trie.md)
- [트리 DP](./concepts/tree-dp.md)
- [수학](./concepts/math.md)
- [분할정복](./concepts/divide-conquer.md)

## DB

- [`db/problem-index.json`](./db/problem-index.json): 373개 문제 Master
- [`db/days.json`](./db/days.json): Day별 문제 배정
- [`db/topics.json`](./db/topics.json): Concept/Topic registry

## 도구

DB 검증:

```bash
python curriculum/scripts/validate_db.py
```

문제 풀이 폴더 생성:

```bash
python curriculum/scripts/new_solution.py 2493
```

시도 코드 생성:

```bash
python curriculum/scripts/new_submission.py 2493
```

## AI Review

- [채점 기준](./ai/grading-rubric.md)
- [코드 리뷰 프롬프트](./ai/grader-prompt.md)
- [힌트 모드](./ai/hint-prompt.md)
- [여러 풀이 비교](./ai/solution-compare-prompt.md)
- [JSON Schema](./ai/review-schema.json)

## 주의

온라인 저지의 실제 채점과 AI의 코드 리뷰는 별개다. AI는 테스트를 실행하지 않았다면 통과를 확정하지 않고, 실제 Judge 결과와 정적 분석 결과를 함께 기록한다.
