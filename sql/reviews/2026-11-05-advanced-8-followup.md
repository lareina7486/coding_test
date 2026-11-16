# 2026-11-05 추가 실전 8문제 — 미커밋 학습 이력 복원

당시 사용자가 푼 **서로 다른 공식 문제 8개**의 결과와 오답 포인트. 전체 원문이 지금 확인되는 경우만 그대로 인용하고, 나머지는 사용자 SQL 파일을 추측해 생성하지 않는다.

| # | 문제 | 결과(확인 범위) | 핵심 내용 |
|---:|---|---|---|
| 1 | [물고기 종류 별 잡은 수 구하기 (293257)](https://school.programmers.co.kr/learn/courses/30/lessons/293257) | 코드 검토 정답 | 어종별 개수 집계·JOIN |
| 2 | 조건에 부합하는 중고거래 상태 조회하기 | 코드 검토 정답 | 거래 상태 CASE |
| 3 | [특정 물고기를 잡은 총 수 구하기 (298518)](https://school.programmers.co.kr/learn/courses/30/lessons/298518) | 코드 검토 정답 | 조건부 어종 COUNT |
| 4 | 조건에 맞는 사원 정보 조회하기 | MySQL 코드 검토 정답 | 사번별 GROUP BY, `emp.EMP_NO` 명시 권장 |
| 5 | [재구매가 일어난 상품과 회원 리스트 구하기 (131536)](https://school.programmers.co.kr/learn/courses/30/lessons/131536) | 최초 문법 오류 후 수정 코드 검토 정답 | `GROUP BY (USER_ID, PRODUCT_ID)` 대신 `GROUP BY USER_ID, PRODUCT_ID` |
| 6 | 자동차 평균 대여 기간 구하기 | 수정 코드 검토 정답 | DATEDIFF+1, HAVING AVG>=7, ROUND(AVG,1) |
| 7 | [연도 별 평균 미세먼지 농도 조회하기 (284530)](https://school.programmers.co.kr/learn/courses/30/lessons/284530) | **사용자 플랫폼 정답 통과 보고** | `DATE_FORMAT(YM,'%Y')` 문자열 대신 `YEAR(YM)` 정수로 수정 |
| 8 | [노선별 평균 역 사이 거리 조회하기 (284531)](https://school.programmers.co.kr/learn/courses/30/lessons/284531) | 수정 코드 검토 정답 | `CONCAT` 문자열을 ORDER BY하지 않고 실제 숫자로 정렬 |

## 원문이 명확한 사용자 SQL

6번 자동차 평균 대여 기간 문제, 사용자가 수정한 SQL:

```sql
SELECT CAR_ID, ROUND(AVG(DATEDIFF(END_DATE,START_DATE)+1),1) AS AVERAGE_DURATION
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
HAVING AVG(DATEDIFF(END_DATE,START_DATE)+1) >= 7
ORDER BY AVERAGE_DURATION DESC, CAR_ID DESC
```

7번 수정 핵심: `DATE_FORMAT(YM,'%Y')` 대신 `YEAR(YM)`; 플랫폼 통과 보고. 실제 SQL 전체는 확인되지 않아 생성하지 않음.

8번 수정 정렬식: `ORDER BY ROUND(SUM(D_BETWEEN_DIST),1) DESC` (사용자 수정). 기존 `TOTAL_DISTANCE`는 단위를 `CONCAT`으로 붙인 문자열이므로 문자열 기준 정렬 위험. 원래 숫자 `SUM(D_BETWEEN_DIST)` 정렬이 더 명확할 수 있다는 대안 설명.

## 중복 집계·출처 주의

- 이 8개는 이미 이전에 최초 시도한 문제이므로 **현재 81/106에 중복으로 추가하지 않음**.
- SQL 원문을 모두 복구하지 못해 **상태·오답 이력·복구 가능한 일부 원문**만 남김. AI가 새로 작성한 SQL을 사용자 제출문으로 저장하지 않음.
