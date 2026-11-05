# CH10 — 서브쿼리 · CTE · UNION · 재귀 CTE (후반부 심화 이관)

- 기존 CH05 서브쿼리는 사용자의 요청에 따라 날짜·조건 분기, 집계/JOIN, 비트 연산, 실무 SQL, 윈도우 함수 학습 이후에 재개.
- 2026-11-05까지 개념 설명과 퀴즈 훈련은 일부 수행했지만 **공식 문제 직접 제출은 없음**.
- 퀴즈 과정: ROUND 1 객관식 7/8 정답, ROUND 2 단답·빈칸 4.5/8점(부분점수 포함), ROUND 2.5 보충 3/3 정답, ROUND 3 결과 예측 퀴즈 출제(제출 확인 없음).
- 서브쿼리 유형: 스칼라·컬럼·행·테이블, 상관·비상관, `IN`, `EXISTS`, `NOT EXISTS`, NULL 함정, 파생 테이블.
- 추가 학습 예정: `WITH`·CTE, `UNION`/`UNION ALL`, 재귀 CTE, 그룹별 최댓값 등.

## 재개 시 같은 주제 묶음으로 풀 공식 문제

1. [ROOT 아이템 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/273710) · Lv.2
2. [업그레이드 된 아이템 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/273711) · Lv.2
3. [업그레이드 할 수 없는 아이템 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/273712) · Lv.3
4. [즐겨찾기가 가장 많은 식당 정보 출력하기](https://school.programmers.co.kr/learn/courses/30/lessons/131123) · Lv.3
5. [물고기 종류 별 대어 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/293261) · Lv.3

- 원칙: 사용자 풀이 전 모범 SQL 비공개, 같은 주제는 한 번에 풀이. CH10 공식 문제 완료 시 챕터 단위로 기록.
