# 남은 32문제 · 2그룹 날짜·기간 계산 (진행 중)

동기화: 2026-11-16 · MySQL · **1/3문제 통과**

| 순서 | 문제 | 상태 |
|---:|---|---|
| 1 | [157340 자동차 대여중 / 대여 가능 여부](https://school.programmers.co.kr/learn/courses/30/lessons/157340) | **플랫폼 통과(사용자 보고)** |
| 2 | [151141 자동차 대여 기록 별 대여 금액](https://school.programmers.co.kr/learn/courses/30/lessons/151141) | **미제출**·다중 JOIN 수업 완료 |
| 3 | [157339 특정 기간 대여 가능한 자동차들의 대여비용](https://school.programmers.co.kr/learn/courses/30/lessons/157339) | **미제출** |

## 157340 최초 오답부터 최종 통과까지

- 첫 시도: `IF(MAX(END_DATE) > '2022-10-16', '대여중', '대여 가능')`. 가장 늦은 반납일만으로는 10월 16일 실제 대여 여부를 판별하지 못함.
- 재도전: `COUNT('2022-10-16' BETWEEN START_DATE AND END_DATE)` 사용. 불리언 TRUE=1과 FALSE=0 모두 NULL이 아니어서 COUNT에 포함됨. [사용자 오답 원문](../attempts/programmers/157340-count-attempt.sql).
- **최종 사용자 SQL**: `SUM('2022-10-16' BETWEEN START_DATE AND END_DATE)>=1`, `CASE` + `GROUP BY CAR_ID` + `ORDER BY CAR_ID DESC`. [최종 원문](../solutions/programmers/157340.sql). 사용자 프로그래머스 통과 보고.
- 통과 후 배운 대안: `MAX(날짜조건)`, `COUNT(CASE WHEN 날짜조건 THEN 1 END)`, 기준일 대여 중인 CAR_ID를 반환하는 `IN (SELECT ...)` 서브쿼리. 강의용 대안이지 사용자 제출 원문은 아님.
- 157340은 이미 과거 최초 시도한 문제이므로 **재도전 중복 집계하지 않음**.

## 151141 개념 수업 완료, SQL 미제출

세 테이블:
- `CAR_RENTAL_COMPANY_CAR`: CAR_ID, CAR_TYPE, DAILY_FEE.
- `CAR_RENTAL_COMPANY_RENTAL_HISTORY`: HISTORY_ID, CAR_ID, START_DATE, END_DATE.
- `CAR_RENTAL_COMPANY_DISCOUNT_PLAN`: CAR_TYPE, DURATION_TYPE, DISCOUNT_RATE.

원리:
1. 트럭의 각 대여 기록을 기준으로 `CAR_ID`로 차량과 JOIN한다.
2. `DATEDIFF(END_DATE,START_DATE)+1`은 대여 시작일·종료일 모두 포함한 일수다.
3. 구간은 1~6일 할인 없음, 7~29일 7일 이상, 30~89일 30일 이상, 90일 이상 90일 이상 할인 적용.
4. 할인 정책은 차종과 해당 기간 구간 **두 조건 모두** 매칭. 차종만 JOIN하면 불필요한 중복 행 발생.
5. 할인이 없는 6일 이하 기록도 유지하려면 할인 정책 연결에 `LEFT JOIN` 고려. 할인율 NULL은 `COALESCE(DISCOUNT_RATE,0)`.
6. 금액: 일일 요금 × 대여 일수 × (1 - 할인율/100), 정수 부분, `FEE DESC, HISTORY_ID DESC`.

## 다중 JOIN 처음 배움

- `USERS JOIN ORDERS JOIN PRODUCTS`: 테이블이 하나 늘 때마다 `JOIN ... ON ...` 추가.
- 새 테이블을 꼭 바로 앞 테이블과 연결할 필요는 없고 이미 참조 가능한 이전 테이블과 연결 가능.
- INNER JOIN과 LEFT JOIN을 혼합할 수 있으며, LEFT JOIN의 오른쪽 테이블 조건을 WHERE에서 강제하면 행 보존이 깨질 수 있음.
- JOIN 관계가 1:N이면 결과 행이 늘어남. 정확한 키와 연결 조건 확인.

151141·157339 미제출이며 2그룹 전체 완료 전. 이번 기록은 사용자의 **전체 중간 경과 동기화 요청**에 따른 스냅샷이다.
