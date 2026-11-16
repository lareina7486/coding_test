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

## 2026-11-16 추가 업데이트 — 서브쿼리 직접 풀이 및 개념 진전

> 앞부분의 '공식 서브쿼리 문제 미제출'은 **2026-11-05 당시 시점**의 기록. 이후 진전은 아래가 최신이다.

- [164671 조회수가 가장 많은 중고거래 게시판의 첨부파일 조회하기](../solutions/programmers/164671.sql): **사용자가 처음으로 파생 테이블 서브쿼리를 직접 작성하고 플랫폼 정답 통과 보고**. 최고 조회수 게시글을 `FROM (SELECT * FROM USED_GOODS_BOARD ORDER BY VIEWS DESC LIMIT 1) AS board`로 먼저 선택하고, 이후 `USED_GOODS_FILE`과 JOIN하여 모든 파일을 반환.
- [131116 식품분류별 가장 비싼 식품의 정보 조회하기](../attempts/programmers/131116-initial.sql): `GROUP BY CATEGORY`와 `MAX(PRICE)`로 비집계 `PRODUCT_NAME`을 올바르게 선택할 수 없다는 사실을 학습. 최초 잘못된 SQL 원문을 오답 초안으로 보관. **정답 통과는 아직 아님**.
- [131123 즐겨찾기가 가장 많은 식당 정보 출력하기](https://school.programmers.co.kr/learn/courses/30/lessons/131123): 음식 종류별 최고 `FAVORITES`와 실제 식당 행을 조회하는 문제로 131116과 같은 패턴. **설명만 진행·미제출**.
- 그룹별 최고가 행의 여러 접근: `MAX` 파생 테이블을 원본과 JOIN(그룹 키와 최댓값 두 개 매칭), 상관 스칼라 서브쿼리, 튜플 `IN`, `NOT EXISTS`(더 비싼 행 없음), `RANK() OVER(PARTITION BY...)`, 자기 자신 `LEFT JOIN`(더 비싼 행 없는 것). 모두 **강의 예시이지 사용자 풀이 원문이 아님**.
- `IN` 서브쿼리와 `EXISTS`/`NOT EXISTS` 비교, `SELECT 1`의 의미, `NOT IN`과 NULL 함정 학습. [273711 업그레이드 된 아이템](https://school.programmers.co.kr/learn/courses/30/lessons/273711)과 [273712 업그레이드할 수 없는 아이템](https://school.programmers.co.kr/learn/courses/30/lessons/273712)은 아직 **미제출**.
- WHERE/SELECT 상관 서브쿼리는 바깥 테이블 별칭 참조가 가능. 일반 FROM 파생 테이블은 같은 FROM 절의 다른 테이블 참조 불가. MySQL 8.0.14+ `LATERAL`로 참조 가능.
- 컬럼 이름이 양쪽 JOIN 테이블에 존재하면 `info.ITEM_ID`처럼 별칭 명시, 유일한 이름은 생략 가능. `INNER JOIN`으로 같게 조인한 두 ID 값은 같으나 `LEFT JOIN`에서 오른쪽 ID는 NULL이 될 수 있음.
- [전체 32문제 유형별 로드맵](remaining-32-groups-overview.md)과 [종합 개념 노트](sql-core-concept-notes-2026-11.md)에도 반영.
