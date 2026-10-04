# Solutions

문제별 여러 풀이를 저장한다.

```text
solutions/boj/2493/
├─ README.md          # 접근법 비교
├─ solution-01.py     # 대표 풀이
├─ solution-02.py     # 대안 풀이
└─ pitfalls.md        # 틀린 이유/실수
```

폴더 생성:

```bash
python curriculum/scripts/new_solution.py 2493
```

원칙:

1. `solution-01.py`는 가장 먼저 재현할 대표 풀이
2. `solution-02.py`부터는 다른 알고리즘, 더 읽기 쉬운 구현, Python 특화 풀이 등
3. README에는 시간/공간복잡도와 어떤 풀이를 외울지 기록
4. 다른 사람 풀이를 복사만 하지 않고 핵심 차이를 한 문장으로 설명
