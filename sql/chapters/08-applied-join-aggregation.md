# CH08 — 실무형 JOIN·집계 응용 (추가 실전)

| 문제 | 사용자 보고 상태 | SQL 기록 |
|---|---|---|
| [131532 년·월·성별별 구매 회원 수](https://school.programmers.co.kr/learn/courses/30/lessons/131532) | 최초 `COUNT(*)` 코드 오류. 수정 `COUNT(DISTINCT info.USER_ID)` **코드 검토 정답**. 수정 SQL 플랫폼 재채점 보고는 없음 | [수정본](../solutions/programmers/131532.sql), [최초 초안](../attempts/programmers/131532-count-initial.sql) |
| [59045 보호소에서 중성화한 동물](https://school.programmers.co.kr/learn/courses/30/lessons/59045) | **플랫폼 정답 통과(사용자 보고)** | [59045.sql](../solutions/programmers/59045.sql) |
| [131117 5월 식품들의 총매출](https://school.programmers.co.kr/learn/courses/30/lessons/131117) | **플랫폼 정답 통과(사용자 보고)** | [131117.sql](../solutions/programmers/131117.sql) |
| [133027 주문량이 많은 아이스크림들](https://school.programmers.co.kr/learn/courses/30/lessons/133027) | **미제출·풀이 중 보류** | 없음 |
| [284529 부서별 평균 연봉 조회하기](https://school.programmers.co.kr/learn/courses/30/lessons/284529) | **플랫폼 정답 통과(사용자 보고)**, 체감 쉬움 · 기존 커밋에 저장 | [284529.sql](../solutions/programmers/284529.sql) |

## SQL 논리 및 대안 풀이

- 131532: 1:N JOIN 이후 한 회원이 같은 월에 여러 번 구매할 수 있으므로 `COUNT(*)`는 구매 기록 수, `COUNT(DISTINCT info.USER_ID)`가 월별 실구매 회원 수. 최초 입력의 플랫폼 '정답 통과' 라벨은 코드 내용과 모순되므로, **현재 수정 SQL은 코드 검토 정답으로만 판정**.
- 59045: 사용자 SQL의 `LIKE 'Intact%'`와 `LIKE 'Spayed%'` 또는 `LIKE 'Neutered%'`는 정확. `REGEXP '^(Spayed|Neutered)'`, `LEFT`, `INSTR` 대안 학습. 포함 검사와 접두어 검사의 의미 차이 주의.
- 131117: 사용자 제출은 `SUM(product.PRICE*orders.AMOUNT)`. 별도로 `SUM(orders.AMOUNT)*product.PRICE`도 같음을 직접 발견. 그룹별 상품 가격이 일정할 때 분배법칙으로 동일하나 주문별 가격이 다를 수 있으면 행별 가격 × 수량을 합산해야 함.
- 날짜 필터는 `PRODUCE_DATE >= '2022-05-01' AND PRODUCE_DATE < '2022-06-01'`로 반열린 구간. DATETIME의 마지막 날짜 시간대를 놓치지 않으며 일반 인덱스에 유리할 수 있음.
- 133027: 상반기·7월 주문량 합산 상위 3개 맛 문제. 7월 같은 맛 여러 행 존재 가능. **직접 풀이 SQL 미제출**.
- 284529: `HR_DEPARTMENT`과 `HR_EMPLOYEES` JOIN 후 부서별 `ROUND(AVG(SAL),0)`, AVG_SAL 내림차순. 별도 사용자 SQL과 난이도 기록 유지.

## 실무 핵심 개념 함께 학습

`COUNT(*)` vs `COUNT(col)` vs `COUNT(DISTINCT col)`; JOIN 카디널리티 1:N·N:M과 중복 집계; `YEAR()` 함수를 적용한 날짜 필터와 범위 검색의 인덱스 차이; `EXPLAIN`에서 `type`, `possible_keys`, `key`, `rows` 확인.
