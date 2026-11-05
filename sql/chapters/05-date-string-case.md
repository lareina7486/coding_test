# CH05 — 날짜·문자열·CASE (2026-11-05 첫 번째 실전 묶음 완료)

- 환경: MySQL, [프로그래머스 SQL 고득점 Kit](https://school.programmers.co.kr/learn/challenges?tab=sql_practice_kit)
- 학습 범위: `QUARTER()`, `CONCAT()`, `CASE`, `IS NULL`, 날짜 비교, `MONTH()`, `DISTINCT`, JOIN, 날짜 차이 정렬
- 이번 신규 공식 문제 **4개**; 사용자 SQL 원문은 각 `.sql`에 저장.
- **묶음 완료 ≠ 챕터 전체 완료**. 이후 같은 CH05의 문자열 가공·날짜 표현 실전을 이어갈 예정.
- 플랫폼 통과 여부는 사용자가 직접 보고한 내용만 반영하며 온라인 SQL 실행을 대신하지 않았음.

## 공식 문제 및 상태

| 문제 | 공식 링크 | 파일 | 검증 상태 |
| --- | --- | --- | --- |
| 분기별 분화된 대장균의 개체 수 구하기 | [299308](https://school.programmers.co.kr/learn/courses/30/lessons/299308) | [299308.sql](../solutions/programmers/299308.sql) | **사용자 프로그래머스 통과 보고**. 첫 제출 정렬식 보완 후 재제출 완료 |
| 조건별로 분류하여 주문상태 출력하기 | [131113](https://school.programmers.co.kr/learn/courses/30/lessons/131113) | [131113.sql](../solutions/programmers/131113.sql) | 코드 검토 정답 · 플랫폼 미채점 |
| 대여 기록이 존재하는 자동차 리스트 구하기 | [157341](https://school.programmers.co.kr/learn/courses/30/lessons/157341) | [157341.sql](../solutions/programmers/157341.sql) | 코드 검토 정답 · 플랫폼 미채점 |
| 오랜 기간 보호한 동물(2) | [59411](https://school.programmers.co.kr/learn/courses/30/lessons/59411) | [59411.sql](../solutions/programmers/59411.sql) | 기본 풀이 적합 · 시간 정밀도 개선 권장 · 플랫폼 미채점 |

## 직접 수정한 내용·오답 기록

### 299308 · 분기별 분화된 대장균의 개체 수 구하기

첫 사용자 SQL:

```sql
SELECT CONCAT(QUARTER(DIFFERENTIATION_DATE), 'Q') AS QUARTER, COUNT(*) AS ECOLI_COUNT
FROM ECOLI_DATA
GROUP BY QUARTER
ORDER BY QUARTER(DIFFERENTIATION_DATE)
```

- 기존 정렬식은 그룹 기준이 아닌 원본 날짜 컬럼을 다시 참조해 모호성을 일으킬 수 있음.
- 수정한 사용자 제출: `ORDER BY QUARTER` (SELECT 결과의 별칭, `1Q`~`4Q` 순서 유지).
- 사용자는 이 수정 SQL로 **프로그래머스 정답 통과**를 보고함.

### 131113 · 조건별로 분류하여 주문상태 출력하기

- `CASE`에서 `OUT_DATE IS NULL`을 우선 처리; 출고 날짜가 기준일 이하라면 출고완료, 이후라면 출고대기로 분기.
- `OUT_DATE` 컬럼은 DATE; 사용자 작성 코드가 공식 출력 조건에 맞는 것으로 검토됨.
- 플랫폼 통과 확인 없음.

### 157341 · 대여 기록이 존재하는 자동차 리스트 구하기

- `INNER JOIN`으로 세단과 10월 시작 대여를 연결하고 `DISTINCT`로 중복 자동차 ID 제거.
- `MONTH(START_DATE)=10`은 서로 다른 연도의 10월을 모두 포함하며 공식 요구사항과 부합.
- 플랫폼 통과 확인 없음.

### 59411 · 오랜 기간 보호한 동물(2)

- `INNER JOIN`으로 입양 이력 있는 동물에 한정; 보호 기간을 내림차순 정렬해 상위 2개 추출.
- `DATEDIFF(outs.DATETIME,ins.DATETIME)`는 시간·분·초를 무시해 동일 날짜 차이 내에서 순위가 달라질 수 있음. 정확한 보호 기간이 필요한 경우 시각까지 반영하는 정렬식을 고려.
- 온라인 채점 여부 미확인. **확정 플랫폼 정답으로 기록하지 않음.**

## 이후 CH05 계획

- 문자열 가공: `CONCAT`, `SUBSTR`, `LEFT`, `RIGHT`, `REGEXP` 등
- 날짜 표현과 형식 확인: `YEAR` vs `DATE_FORMAT`, `DATEDIFF` vs `TIMESTAMPDIFF`
- CASE·중복 제거 응용 문제 몇 개를 추가해 문제 유형별 부족한 부분을 보완.

## 학습 공통 주의점

1. `GROUP BY` 이후 정렬은 그룹 키 또는 집계 결과를 우선 사용.
2. 출력 표시용 문자열과 수치/날짜 계산값을 구분.
3. 플랫폼 정답 여부와 자체 코드 리뷰를 혼동하지 않기.
