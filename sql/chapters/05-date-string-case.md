# CH05 — 날짜·문자열·CASE (2026-11-06 두 번째 실전 묶음까지 완료)

- 환경: MySQL, [프로그래머스 SQL 고득점 Kit](https://school.programmers.co.kr/learn/challenges?tab=sql_practice_kit)
- 학습 범위: `QUARTER()`, `CONCAT()`, `CASE`, `IS NULL`, 날짜 비교, `MONTH()`, `DISTINCT`, JOIN, 날짜 차이 정렬
- 첫 묶음 신규 공식문제 **4개**, 두 번째 묶음 **4문제** 중 신규 1개·기존 문제 재풀이 3개. 사용자 최신 SQL 원문은 각 `.sql`에 저장.
- **사전에 계획한 CH05 필수 실전 8/8문제 완료**. 플랫폼 통과 여부는 아래 문제별로 구분. 다음은 CH06 응용.
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

## CH05 두 번째 실전 묶음 (2026-11-06)

| 공식 문제 | 문제 URL | 제출 SQL 파일 | 검증 상태 / 유형 |
| --- | --- | --- | --- |
| 조건에 맞는 사용자 정보 조회하기 · Lv.3 | [164670](https://school.programmers.co.kr/learn/courses/30/lessons/164670) | [164670.sql](../solutions/programmers/164670.sql) | **사용자 플랫폼 정답 통과 보고** · 이번 신규 도전 +1 |
| 자동차 대여 기록에서 장기/단기 대여 구분하기 · Lv.1 | [151138](https://school.programmers.co.kr/learn/courses/30/lessons/151138) | [151138.sql](../solutions/programmers/151138.sql) | **사용자 플랫폼 정답 통과 보고** · 기존 보완 문제 |
| 이름에 el이 들어가는 동물 찾기 · Lv.2 | [59047](https://school.programmers.co.kr/learn/courses/30/lessons/59047) | [59047.sql](../solutions/programmers/59047.sql) | **사용자 플랫폼 정답 통과 보고** · CH01 기존 정렬 보완 |
| 3월에 태어난 여성 회원 목록 출력하기 · Lv.2 | [131120](https://school.programmers.co.kr/learn/courses/30/lessons/131120) | [131120.sql](../solutions/programmers/131120.sql) | **사용자 플랫폼 정답 통과 보고** · 기존 날짜 표현 보완 |

### 두 번째 묶음 해설·검토

- **164670**: 회원 ID별 게시물 수 `GROUP BY`·`HAVING COUNT(*)>=3`, `TRIM(CONCAT(...))`로 주소 조합, `SUBSTR`로 3-4-4 전화번호 표현. `STREET_ADDRESS2`가 NULL인 경우 `CONCAT` 결과도 NULL인 일반적 특성은 참고사항으로만 기록; 사용자가 제출한 원문을 임의 수정하지 않음.
- **151138**: `DATEDIFF(END_DATE,START_DATE)+1`로 양 끝일 포함, `DATE_FORMAT`으로 날짜 출력 요구사항 준수, `CASE` 기간 30일 기준, `HISTORY_ID DESC`.
- **59047**: `LIKE '%el%' AND ANIMAL_TYPE='Dog'`, `ORDER BY NAME, ANIMAL_ID`는 공식 요구 정렬과 일치함. 사용자의 현재 제출 SQL에는 **보완할 부분 없음**. CH01의 과거 정렬 오류 해결.
- **131120**: `MONTH(DATE_OF_BIRTH)=3`, `GENDER='W'`, `TLNO IS NOT NULL`, `DATE_FORMAT(...,'%Y-%m-%d')` 출력으로 통과.

### 누적 집계 주의

- 신규 도전은 164670 **1문제만** 추가하며 나머지 3문제는 이전 도전의 복습/수정.
- 이전 총 67개 → 현재 **68개** 고유 공식 문제 도전.
- 두 번째 묶음 4개 모두 **사용자가 프로그래머스 통과를 보고**함. 앱에 직접 실행 요청한 것은 아님.

## 마무리

- 계획된 8문제 마무리: `CONCAT`, `SUBSTR`, `DATE_FORMAT`, `CASE`, `QUARTER`, `DATEDIFF`, `GROUP BY`, `HAVING`, `JOIN` 핵심 활용.
- `LEFT`, `RIGHT`, `CONCAT_WS`, `REGEXP`, `TIMESTAMPDIFF`는 유관 개념 소개를 마쳤으며, 필요하면 후속 복습에 배치.
- 다음 학습: CH06 `GROUP BY`·`JOIN` 응용.

## 학습 공통 주의점

1. `GROUP BY` 이후 정렬은 그룹 키 또는 집계 결과를 우선 사용.
2. 출력 표시용 문자열과 수치/날짜 계산값을 구분.
3. 플랫폼 정답 여부와 자체 코드 리뷰를 혼동하지 않기.
