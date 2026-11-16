# CH09 — 윈도우 함수 개념 도입 (공식 풀이 미제출)

- `GROUP BY`는 여러 행을 집계 결과로 축약하지만 **윈도우 함수는 원래 행을 유지하면서 계산**한다.
- `OVER (PARTITION BY DEPT)`: 부서별 합계/평균 계산 결과를 각 직원 행에 붙이기. `PARTITION BY`는 계산 범위 설정.
- `ROW_NUMBER()`: 동점에도 다른 번호, `RANK()`: 동점 뒤 번호를 건너뜀, `DENSE_RANK()`: 동점 뒤에도 다음 번호 연속.
- `NTILE(4) OVER (ORDER BY SIZE_OF_COLONY DESC)`: 정렬된 대장균 크기를 4개 구간으로 나누어 상위 사분위 분류.
- 윈도우 `OVER(... ORDER BY ...)`는 순위 계산 순서이고 SQL 맨 뒤의 `ORDER BY`는 최종 출력 순서.
- 공식 문제: [301649 대장균의 크기에 따라 분류하기 2](https://school.programmers.co.kr/learn/courses/30/lessons/301649) (Lv.3), **SQL 미제출**. 개념 학습을 문제 풀이 완료로 계산하지 않는다.
