# SQL 학습 기록 — 실전 문제 중심, 반복 회독

**업데이트: 2026-11-07 · MySQL 기반**  
목표: 프로그래머스 SQL 고득점 Kit의 주요 문법 습득 → 응용 SQL 실력 확보 → 이후 LeetCode/SolveSQL 및 PCSQL 수준 문제 선택 학습.

## 운영 원칙

1. **150문제를 숫자로 채우는 고정 목표는 폐기.** 그때그때 부족한 개념에 맞추어 실제 공식 문제를 선정합니다.
2. 새로운 문법은 **문제에 앞서 설명**하고, 난이도는 이해도에 따라 조절합니다.
3. 기본 문법을 이해시키는 아주 쉬운 자체 예제는 허용. 이외의 연습 문제는 실제 사이트의 원문과 URL 사용.
4. 사용자가 **직접 제출한 SQL 원문**을 저장. AI가 제안한 개선안/모범답안과 섞지 않습니다.
5. 플랫폼 통과 보고 / 코드상 적합 / 재풀이 필요 / 미제출을 별도 표기. 실제 플랫폼을 대신 실행한 적은 없으므로 실행 통과를 추정하지 않습니다.
6. 평소에는 **챕터 완료 시 1회 일괄 커밋**. 2026-11-04에는 사용자의 명시적 요청에 따라 수업 종료 시점의 **전체 학습 스냅샷을 1회 커밋**합니다.
7. 이미 푼 문제의 복습은 신규 문제 도전 수로 중복 계산하지 않습니다.

## 진행 현황 (2026-11-06)

| 과정 | 상태 | 메모 |
| --- | --- | --- |
| CH01 SELECT·WHERE·정렬 | **기록된 15문제 점검 완료** | 09번 [이름에 el이 들어가는 동물 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/59047) 2026-11-06 사이트 통과 보고; [진행 기록](chapters/01-select-where-progress.md) |
| CH02 NULL·DISTINCT·COUNT | **학습 완료** | 16~21 여섯 문제, [요약](chapters/02-null-distinct-count.md) |
| CH03 집계·GROUP BY·HAVING | **학습 완료** | 22~26 다섯 문제, [요약](chapters/03-aggregation-group-by-having.md) |
| CH04 JOIN | **학습 완료** | 27~31 다섯 문제, [요약](chapters/04-joins.md) |
| **Lv.1/Lv.2 추가 실전** | **24문제 도전 / 원문 SQL 23개 저장** | [당일 학습기록](reviews/2026-11-04-extra-practice.md). 1문제는 미제출 |
| CH05 날짜·문자열·CASE | **계획된 실전 8/8문제 완료** | [8문제 SQL·채점·오답 기록](chapters/05-date-string-case.md): 첫 묶음 4개 + 두 번째 묶음 4개(모두 사용자 플랫폼 통과 보고) |
| CH06~09 응용·비트연산·실무·윈도우 함수 | 예정 | 주제별 공식 문제 연습 |
| CH10 서브쿼리·CTE·UNION·재귀 CTE | **후반부 심화로 보류** | [기존 서브쿼리 학습 기록](chapters/10-subqueries-cte-progress.md), 개념 퀴즈까지 진행·공식 문제 미제출 |

**누적 도전 문제: 68개** = 이전 67개 + 신규 [조건에 맞는 사용자 정보 조회하기(164670)](https://school.programmers.co.kr/learn/courses/30/lessons/164670) 1개. 2026-11-06 CH05 두 번째 묶음의 나머지 3개는 이전에 도전한 문제의 **재풀이**로 중복 집계하지 않습니다.  
이 수치는 **도전한 서로 다른 공식 문제 수**이며, 정답/제출 통과 수가 아닙니다. 기존 대화의 52개 카운트는 '성분으로 구분한 아이스크림 총 주문량' 1개를 추가로 세지 않은 것이므로 정정합니다. 이번 '3월에 태어난 여성 회원'과 '월별 잡은 물고기 수 구하기'는 각각 별도 신규 문제입니다.

## 현재 다시 풀거나 확인할 문제

- Lv.1 [특정 형질을 가지는 대장균 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/301646): 비트 AND 학습 후 최초 제출
- Lv.2 [카테고리 별 상품 개수 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/131529): ORDER BY CATEGORY로 안정성 재검토(사용자 정답 보고는 그대로 유지)
- Lv.2 [성분으로 구분한 아이스크림 총 주문량](https://school.programmers.co.kr/learn/courses/30/lessons/133026): LEFT/INNER JOIN의 매칭 가정 확인
- 출력 날짜 형식이 지정된 기타 문제의 사이트 통과 여부는 필요 시 추가 확인

## 이후 학습 지도 (문항 수·마감일 강제하지 않음)

| 순서 | 학습 주제 | 새 문법 / 확인할 내용 | 실제 공식 문제 후보 |
| --- | --- | --- | --- |
| 1 | **CH05 날짜·문자열·CASE** | QUARTER, DATE_FORMAT, YEAR/MONTH, DATEDIFF, CONCAT, SUBSTR, CASE, NULL | **8/8 공식문제 풀이 완료**, [기록](chapters/05-date-string-case.md) |
| 2 | CH06 GROUP BY·JOIN 응용 심화 | 조건부 집계, 다중 JOIN, anti-join, 중복 행 제거 | 미풀이 공식 Lv.2~3 문제 |
| 3 | CH07 비트 연산·조건 분류 | 비트 AND(&), 마스크 판별, CASE 분류 | [특정 형질을 가지는 대장균 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/301646) 등 |
| 4 | CH08 실무 SQL | PK/FK, 인덱스, EXPLAIN, INSERT·UPDATE·DELETE, 트랜잭션 | 실무 실습 |
| 5 | CH09 윈도우 함수 | OVER, PARTITION BY, ROW_NUMBER, RANK, LAG/LEAD, 누적합 | Lv.3 응용 및 LeetCode/SolveSQL |
| 6 | **CH10 서브쿼리·CTE·집합·재귀** | Scalar/IN/EXISTS/NOT EXISTS, 상관, WITH, UNION, WITH RECURSIVE | [서브쿼리 진행 기록](chapters/10-subqueries-cte-progress.md)과 기존 공식 문제 후보 |
| 7 | 응용 2회독 | Lv.3~Lv.5 문제, 복합 SQL, LeetCode SQL 50, SolveSQL | 약한 주제 중심, 신규/복습 구별 |

이 로드맵의 **단계와 문항은 필요에 따라 조절 가능**합니다. 고급 실습은 새 문법 소개 후 시작합니다.

## 디렉터리

- `sql/chapters/`: 완료/진행 챕터 기록
- `sql/solutions/programmers/`: 직접 작성한 공식 문제 SQL
- `sql/reviews/`: 여러 챕터에 걸친 추가 풀이·복습 기록

## 공식 문제 사이트

- [프로그래머스 SQL 고득점 Kit](https://school.programmers.co.kr/learn/challenges?tab=sql_practice_kit)
- [LeetCode SQL 50](https://leetcode.com/studyplan/top-sql-50/)
- [SolveSQL](https://solvesql.com/problems/)

## 2026-11-06 기록 범위 주의

- 공식 신규 도전 수는 현재까지 **68문제** (실제 사이트 정답 통과 수와 다름).
- 11/05 앞선 8개 응용 실전 문제는 이 커밋의 SQL 파일에 포함하지 않았으며, 추후 해당 주제 묶음에서 상태별로 보관 예정.
- CH05의 두 차례 묶음 총 8문제는 사용자 SQL 원문과 채점 상태를 [별도 챕터 파일](chapters/05-date-string-case.md)로 기록. 2026-11-06 두 번째 묶음은 네 문제 모두 사용자 플랫폼 통과 보고.
- 서브쿼리 학습 기록은 CH10으로 이관, 공식 서브쿼리 문제는 아직 미제출.

## 2026-11-06 다음 학습: CH06 GROUP BY·JOIN 응용

- 바로 이어서: [가격대 별 상품 개수](https://school.programmers.co.kr/learn/courses/30/lessons/131530), [카테고리 별 도서 판매량](https://school.programmers.co.kr/learn/courses/30/lessons/144855), [조건에 맞는 사용자와 총 거래금액](https://school.programmers.co.kr/learn/courses/30/lessons/164668), [자동차 대여중/대여 가능 여부](https://school.programmers.co.kr/learn/courses/30/lessons/157340), [저자 별 카테고리 별 매출액](https://school.programmers.co.kr/learn/courses/30/lessons/144856) (Lv.4 도전).
- 서브쿼리 의존 문제는 CH10 후반부로 미룸. CH06 문제는 사용자가 직접 작성하기 전 모범 SQL 비공개.

## 2026-11-07 추가 실전 기록

- [부서별 평균 연봉 조회하기 · Lv.3 (284529)](https://school.programmers.co.kr/learn/courses/30/lessons/284529): 사용자 직접 SQL 정답 통과 보고 · 체감 **쉬움**. [원문 SQL](solutions/programmers/284529.sql) / [추가 실전 기록](reviews/2026-11-07-extra-practice.md).
- [즐겨찾기가 가장 많은 식당 정보 출력하기 · Lv.3 (131123)](https://school.programmers.co.kr/learn/courses/30/lessons/131123): 현재 **서브쿼리 개념 학습 중, SQL 미제출**. 신규 도전으로 집계하지 않음.
- 이전 README의 **68문제**는 2026-11-06 저장 당시 기준. 이후 대화에서 추가 도전한 문제와 현재 기록을 합친 사용자 대화상 누적은 **79/106문제 도전** (미완성·오답 시도 포함), 최초 SQL 미작성 **27문제**. 이번 커밋은 **284529만 추가 저장**하고 그 밖의 대화 중 미커밋 풀이 원문을 임의로 생성하지 않음.
- 사용자가 명시적으로 기록을 요청한 284529의 경우 요청에 따라 단독 저장. 다른 보류/미완료 문제는 해당 학습 묶음 완료 시 일괄 기록.
