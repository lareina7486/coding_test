# 2026-11-16 프로그래머스 SQL 학습 내역 전체 동기화

**기준:** 기존 `lareina7486/coding_test` 저장소와 2026-11-16까지의 SQL 학습 대화를 대조. MySQL.

## 전체 수치와 분리 기준

- **프로그래머스 공식 SQL 고득점 Kit 106문제 중 서로 다른 문제 최초 도전 81개(76.4%)**; 최초 도전이 남은 문제 **25개**. 이 숫자는 정답 개수가 아닌 **시도한 문제의 개수**이며, 틀린 뒤 재도전은 추가하지 않음.
- 사용자가 제공한 미완료 대상 32문제에서는 현재 **3개 플랫폼 통과·29개 미완료**. 초기 사용자 목록과 현 진도가 변하므로 이를 106개 중 미도전 수와 혼동하면 안 됨.
- [32문제 유형별 진도표](../chapters/remaining-32-groups-overview.md), [CSV](../tracking/remaining-32.csv).
- 과거 README의 68/106·79/106 기록은 당시 날짜 기준 스냅샷이며 현재 진행률이 아니다.

## 기존에 기록되어 있던 사용자 SQL·학습

- CH01 SELECT·WHERE·정렬, CH02 NULL·DISTINCT, CH03 집계·GROUP BY, CH04 JOIN, CH05 날짜·문자열·CASE는 기존 파일 보존.
- 2026-11-04 Lv.1·Lv.2 추가 실전 24문제 중 원문 SQL 23개는 기존 [당일 기록](2026-11-04-extra-practice.md)에 저장되어 있었음.
- [284529 부서별 평균 연봉](../solutions/programmers/284529.sql)은 이전 커밋에 이미 **사용자 플랫폼 통과·체감 쉬움**으로 기록.
- [273710 ROOT](../solutions/programmers/273710.sql), [164671 첨부파일 조회](../solutions/programmers/164671.sql)은 **1그룹 완료**로 이전 커밋에서 원문과 사용자 통과 상태 기록.
- [2026-11-05 추가 실전 8문제](2026-11-05-advanced-8-followup.md)는 이전 기록에서 빠져 있어 수정·오답·확인 가능한 SQL 일부와 상태를 별도 복원함.

## 이번에 새로 복원한 직접 작성 SQL 원문

| 번호 | 현재 평가 | 사용자 원문 |
|---|---|---|
| 131530 가격대별 상품 개수 | **플랫폼 통과(사용자 보고)** | [131530.sql](../solutions/programmers/131530.sql) |
| 299307 대장균 크기 분류 1 | **플랫폼 통과(사용자 보고)** | [299307.sql](../solutions/programmers/299307.sql) |
| 131532 연월·성별 구매 회원 수 | **수정 SQL 코드 검토 정답 / 수정본 플랫폼 미확인** | [131532.sql](../solutions/programmers/131532.sql) |
| 59045 보호소에서 중성화한 동물 | **플랫폼 통과(사용자 보고)** | [59045.sql](../solutions/programmers/59045.sql) |
| 131117 5월 식품들의 총매출 | **플랫폼 통과(사용자 보고)** | [131117.sql](../solutions/programmers/131117.sql) |
| 157340 대여 중/대여 가능 | **오답 재도전 뒤 플랫폼 통과(사용자 보고)** | [157340.sql](../solutions/programmers/157340.sql) |

원문은 사용자 작성 그대로 저장. 포맷 개선, 모범 SQL, 설명 예제는 사용자 원문 파일에 섞지 않음.

## 실제 오답·초안 6건도 별도 보존

- [301646 첫 비트 연산 오답](../attempts/programmers/301646-first.sql): BIN 사용 · 형질 마스크 오류.
- [301646 두 번째 오답](../attempts/programmers/301646-second.sql): 3번 형질에 마스크 3 사용(실제 마스크 4).
- [276034 개발자 스킬 초기 오답](../attempts/programmers/276034-initial.sql): 동등 JOIN 조건의 문제, 아직 재풀이 보류.
- [131116 최고가 상품명 초기 오답](../attempts/programmers/131116-initial.sql): 그룹별 MAX와 비집계 PRODUCT_NAME 혼용.
- [157340 COUNT 불리언 오답](../attempts/programmers/157340-count-attempt.sql): FALSE도 COUNT에 포함되는 문제.
- [131532 COUNT(*) 초기 코드](../attempts/programmers/131532-count-initial.sql): 주문 행 수와 중복 없는 구매 회원 수 혼동.

## 원문 미확인 또는 실제 SQL 미제출 — 상태만 기록

- **플랫폼 통과 사용자 보고 / 최종 전체 SQL 원문 현재 확인 불가:** 144855 카테고리별 도서 판매량, 164668 사용자 총 거래금액, 301646 특정 형질 대장균 최종 통과본. 301646은 *오답 2차까지 원문*만 보존함.
- **기존 오답·보류:** 276034 조건에 맞는 개발자, 131116 식품분류별 최고가.
- **미제출·보류:** 144856 저자별 매출액, 301647 부모 형질 대장균, 133027 아이스크림 주문량, 131123 최다 즐겨찾기 식당, 273711 업그레이드 된 아이템, 273712 업그레이드할 수 없는 아이템, 301649 대장균 크기 분류 2 등. 전체 목록은 32문제 진도표 기준.
- **현재 학습 중 151141 자동차 대여 기록별 금액**: 날짜 계산·다중 JOIN·LEFT JOIN·할인 기간·COALESCE·요금 계산을 배웠지만 SQL은 아직 작성하지 않음. 157339는 그다음.
- 이 항목들의 SQL을 AI가 만들어 사용자 제출문이라고 기록하지 않음.

## 개념 및 학습 이력 보존 파일

- [CH06 GROUP BY·JOIN 응용](../chapters/06-group-by-join-application.md)
- [CH07 비트 연산](../chapters/07-bitwise-practice.md)
- [CH08 실무형 SQL](../chapters/08-applied-join-aggregation.md)
- [CH09 윈도우 함수](../chapters/09-window-functions-intro.md)
- [CH10 서브쿼리·CTE 진행·후속 업데이트](../chapters/10-subqueries-cte-progress.md)
- [2그룹 날짜·기간 계산과 157340 오답 이력](../chapters/remaining-32-group-02-date-period.md)
- [핵심 SQL 개념 노트](../chapters/sql-core-concept-notes-2026-11.md): COUNT DISTINCT, JOIN cardinality, 인덱스·EXPLAIN, 상관 서브쿼리·LATERAL, 그룹별 최고가 여러 풀이, 윈도우 함수, BETWEEN·DATEDIFF, 문자열, 컬럼 접두어.

## 앞으로 반드시 지킬 운영 규칙

1. 사용자가 공식 문제를 풀기 **전에는 정답 SQL 공개하지 않기**, 오답에는 힌트 하나씩 단계적으로.
2. **정답 통과 뒤에는 다른 풀이 2~3가지**를 비교해서 설명(방식별 장단점 포함).
3. **문제를 풀 때마다 전체 남은 유형/문제 목록**을 보여주고 유형별 쉬운 순서 유지.
4. 플랫폼 통과 보고 / 코드 검토 정답 / 오답 / 미제출 정확하게 구분.
5. 한 유형의 학습 묶음이 끝나면 GitHub **일괄 커밋**. 전체 학습 기록 업데이트 명시 요청은 예외.
6. 사용자가 직접 작성한 SQL과 문제별 수정 내역·상태·오답·개념을 빠짐없이 남기되 **모르는 최종 SQL은 임의 생성 금지**.

현재 진행: **2그룹 151141** (기본 개념 강의 후 SQL 입력 대기).
