# SQL 학습 기록 — 실전 문제 중심, 반복 회독

**업데이트: 2026-11-04 · MySQL 기반**  
목표: 프로그래머스 SQL 고득점 Kit의 주요 문법 습득 → 응용 SQL 실력 확보 → 이후 LeetCode/SolveSQL 및 PCSQL 수준 문제 선택 학습.

## 운영 원칙

1. **150문제를 숫자로 채우는 고정 목표는 폐기.** 그때그때 부족한 개념에 맞추어 실제 공식 문제를 선정합니다.
2. 새로운 문법은 **문제에 앞서 설명**하고, 난이도는 이해도에 따라 조절합니다.
3. 기본 문법을 이해시키는 아주 쉬운 자체 예제는 허용. 이외의 연습 문제는 실제 사이트의 원문과 URL 사용.
4. 사용자가 **직접 제출한 SQL 원문**을 저장. AI가 제안한 개선안/모범답안과 섞지 않습니다.
5. 플랫폼 통과 보고 / 코드상 적합 / 재풀이 필요 / 미제출을 별도 표기. 실제 플랫폼을 대신 실행한 적은 없으므로 실행 통과를 추정하지 않습니다.
6. 평소에는 **챕터 완료 시 1회 일괄 커밋**. 2026-11-04에는 사용자의 명시적 요청에 따라 수업 종료 시점의 **전체 학습 스냅샷을 1회 커밋**합니다.
7. 이미 푼 문제의 복습은 신규 문제 도전 수로 중복 계산하지 않습니다.

## 진행 현황 (2026-11-04)

| 과정 | 상태 | 메모 |
| --- | --- | --- |
| CH01 SELECT·WHERE·정렬 | **부분 진행** | 01~15 도전; 09 정렬 수정 후 사이트 재확인 필요. 이용 가능한 이전 기록은 [01-select-where-progress.md](chapters/01-select-where-progress.md)에 요약 |
| CH02 NULL·DISTINCT·COUNT | **학습 완료** | 16~21 여섯 문제, [요약](chapters/02-null-distinct-count.md) |
| CH03 집계·GROUP BY·HAVING | **학습 완료** | 22~26 다섯 문제, [요약](chapters/03-aggregation-group-by-having.md) |
| CH04 JOIN | **학습 완료** | 27~31 다섯 문제, [요약](chapters/04-joins.md) |
| **Lv.1/Lv.2 추가 실전** | **24문제 도전 / 원문 SQL 23개 저장** | [당일 학습기록](reviews/2026-11-04-extra-practice.md). 1문제는 미제출 |
| CH05 서브쿼리 | **개념 학습·문제 미제출** | 다음 학습 시작점: 2026-11-05, [진행 기록](chapters/05-subqueries-progress.md) |

**누적 도전 문제: 55개** = CH01~CH04에서 도전 31개 + 추가 신규 24개.  
이 수치는 **도전한 서로 다른 공식 문제 수**이며, 정답/제출 통과 수가 아닙니다. 기존 대화의 52개 카운트는 '성분으로 구분한 아이스크림 총 주문량' 1개를 추가로 세지 않은 것이므로 정정합니다. 이번 '3월에 태어난 여성 회원'과 '월별 잡은 물고기 수 구하기'는 각각 별도 신규 문제입니다.

## 현재 다시 풀거나 확인할 문제

- CH01 09번 정렬 조건 수정 후 최종 플랫폼 판정 확인
- Lv.1 [자동차 대여 기록에서 장기/단기 대여 구분하기](https://school.programmers.co.kr/learn/courses/30/lessons/151138): DATE_FORMAT까지 출력 형식 보완
- Lv.1 [특정 형질을 가지는 대장균 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/301646): 비트 AND 학습 후 최초 제출
- Lv.2 [카테고리 별 상품 개수 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/131529): ORDER BY CATEGORY로 안정성 재검토(사용자 정답 보고는 그대로 유지)
- Lv.2 [3월에 태어난 여성 회원 목록 출력하기](https://school.programmers.co.kr/learn/courses/30/lessons/131120): 생년월일 출력 형식 확인
- Lv.2 [성분으로 구분한 아이스크림 총 주문량](https://school.programmers.co.kr/learn/courses/30/lessons/133026): LEFT/INNER JOIN의 매칭 가정 확인
- 출력 날짜 형식이 지정된 기타 문제의 사이트 통과 여부는 필요 시 추가 확인

## 이후 학습 지도 (문항 수·마감일 강제하지 않음)

| 순서 | 학습 주제 | 새 문법 / 확인할 내용 | 실제 공식 문제 후보 |
| --- | --- | --- | --- |
| 1 | **CH05 서브쿼리** | 스칼라/테이블 서브쿼리, IN, EXISTS, NOT EXISTS, 상관 서브쿼리, NOT IN·NULL | [업그레이드 된 아이템 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/273711), [업그레이드 할 수 없는 아이템 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/273712), [즐겨찾기가 가장 많은 식당 정보 출력하기](https://school.programmers.co.kr/learn/courses/30/lessons/131123) |
| 2 | 날짜·문자열·조건 분기 | DATE_FORMAT, YEAR/MONTH/HOUR, DATEDIFF, LEFT/SUBSTR, CASE, COALESCE, REGEXP | [자동차 평균 대여 기간 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/157342), [조건별로 분류하여 주문상태 출력하기](https://school.programmers.co.kr/learn/courses/30/lessons/131113) 등 실제 문제 |
| 3 | 조건부 집계·JOIN 심화 | 조건부 SUM/COUNT, HAVING, 중복 제거, 다중 JOIN, anti-join, JOIN 매칭 카디널리티 | [저자 별 카테고리 별 매출액 집계하기](https://school.programmers.co.kr/learn/courses/30/lessons/144856) 등 |
| 4 | 집합·CTE | UNION/UNION ALL, WITH, 여러 단계의 가공 | [오프라인/온라인 판매 데이터 통합하기](https://school.programmers.co.kr/learn/courses/30/lessons/131537) 등 |
| 5 | 윈도우 함수 | OVER/PARTITION BY, ROW_NUMBER, RANK, DENSE_RANK, LAG/LEAD, 누적합 | LeetCode/SolveSQL 공식 문제 중 수준에 맞춰 선정 |
| 6 | 재귀 CTE·계층형 관계 | WITH RECURSIVE, 부모·자식 탐색, 종료 조건 | [특정 세대의 대장균 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/301650) 등 |
| 7 | 비트 연산 | 비트 AND (&), 마스크 판별, 논리 우선순위 | 앞서 보류한 [특정 형질을 가지는 대장균 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/301646)부터 진행 |
| 8 | SQL 실무/성능 기초 | PK/FK, 인덱스, EXPLAIN, DB 실행 계획, DML, 트랜잭션/격리 수준 | 별도 실습 + 공식 문제 |
| 9 | 응용 2회독 | Lv.3~Lv.5, 종합 JOIN/집계/서브쿼리, LeetCode SQL 50, SolveSQL | 약한 주제만 선정, 이전 문제는 복습으로 분리 |

이 로드맵의 **단계와 문항은 필요에 따라 조절 가능**합니다. 고급 실습은 새 문법 소개 후 시작합니다.

## 디렉터리

- `sql/chapters/`: 완료/진행 챕터 기록
- `sql/solutions/programmers/`: 직접 작성한 공식 문제 SQL
- `sql/reviews/`: 여러 챕터에 걸친 추가 풀이·복습 기록

## 공식 문제 사이트

- [프로그래머스 SQL 고득점 Kit](https://school.programmers.co.kr/learn/challenges?tab=sql_practice_kit)
- [LeetCode SQL 50](https://leetcode.com/studyplan/top-sql-50/)
- [SolveSQL](https://solvesql.com/problems/)
