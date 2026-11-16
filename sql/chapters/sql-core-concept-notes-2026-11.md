# SQL 핵심 개념 종합 노트 — 2026-11-16

이 파일은 학습한 **개념과 설명**의 기록이다. 강의 예제 SQL은 `solutions/programmers/`의 **사용자가 실제 제출한 SQL 원문**과 구분한다.

## 집계·GROUP BY

- `COUNT(*)`: 전체 행. `COUNT(column)`: NULL이 아닌 행. `COUNT(DISTINCT USER_ID)`: NULL/중복을 제외한 고유 회원 수.
- 1:N JOIN을 하면 한 회원이 주문 건수만큼 여러 행으로 늘 수 있다. `COUNT(*)`와 고유 구매 회원 수를 혼동하지 않는다.
- MySQL은 TRUE=1, FALSE=0. `SUM(조건)`은 참인 행 수를 셀 수 있지만 `COUNT(조건)`은 FALSE(0)도 NULL이 아니어서 포함.
- `GROUP BY`에 `MAX(PRICE)`가 있어도 `PRODUCT_NAME`이 최고가 행에서 선택되는 것은 아니다. `ONLY_FULL_GROUP_BY`에서는 비그룹 비집계 열 참조가 오류일 수 있음.
- `WHERE`는 그룹화 전 행 필터, `HAVING`은 집계된 그룹 필터. MySQL에서는 SELECT 별칭을 ORDER BY/GROUP BY에서 활용할 수 있음.

## JOIN·다중 JOIN·컬럼 수식

- `INNER JOIN`: 양쪽 매칭 데이터만. `LEFT JOIN`: 왼쪽 모든 행을 보존, 매칭 없는 오른쪽 컬럼은 NULL.
- 예: `FROM USERS u JOIN ORDERS o ON u.USER_ID=o.USER_ID JOIN PRODUCTS p ON o.PRODUCT_ID=p.PRODUCT_ID` — JOIN을 하나씩 이어서 세 테이블 연결.
- 새로 JOIN하는 테이블은 반드시 직전 테이블과 연결하지 않아도 되며 이미 범위에 들어온 다른 테이블 컬럼을 ON에서 사용할 수 있음.
- 같은 차종에 7·30·90일 할인 정책이 모두 있을 때 차종만 ON 조건으로 JOIN하면 기록이 중복됨. 해당 대여 기간에 맞는 정책도 함께 검사.
- LEFT JOIN 후 `WHERE right.col = ...` 같은 조건이 NULL 행을 제거하면 보존 의도가 깨질 수 있음.
- 두 테이블에 같은 `ITEM_ID`가 있다면 `info.ITEM_ID`처럼 별칭으로 열을 구분해야 함. 한쪽에만 존재하는 컬럼은 접두어를 생략해도 되지만 실무에서는 명시가 가독성에 유리.
- 별칭을 지정했다면 그 쿼리 범위에서는 별칭을 사용. INNER JOIN에서 ON으로 동일 ID를 매칭한 경우 값이 같으나 LEFT JOIN에서는 오른쪽 ID가 NULL일 수 있음.
- `USING (ITEM_ID)`는 같은 이름의 공통 연결 컬럼을 결합하여 `SELECT ITEM_ID`로 참조할 수 있음.

## 날짜·요금·성능

- `DATEDIFF(END_DATE,START_DATE)+1`: 대여 시작일과 종료일 모두 포함한 일수.
- `BETWEEN`은 양 끝 경계를 포함. 특정 날짜가 START_DATE~END_DATE 안에 있는지 정확히 판별.
- `col >= '2026-01-01' AND col < '2027-01-01'` 반열린 구간은 DATETIME의 마지막 날 시간 누락을 피함.
- `YEAR(col)` 조건은 일반 B-tree 날짜 인덱스를 바로 활용하기 어려울 수 있다. 인덱스·데이터·옵티마이저에 따라 달라지므로 무조건 느리다고 단정할 수는 없음.
- `EXPLAIN` 실행 계획의 `type`, `possible_keys`, `key`, `rows` 확인; `EXPLAIN ANALYZE`는 실제 실행 정보를 제공.
- `COALESCE(DISCOUNT_RATE,0)`로 할인 정책 NULL을 0% 처리. 최종 대여금액은 일일요금 × 대여일수 × (1 - 할인율/100).
- `FLOOR`, `TRUNCATE(...,0)`는 정수 표현에 쓰이지만 음수·소수 처리에 차이 가능. 문제 출력 규칙 우선.

## 문자열·데이터 타입

- `CONCAT`는 첨부파일 경로 문자열 조합. `LIKE 'Intact%'`는 접두어 검사; `REGEXP`는 정규식; `INSTR`은 부분 문자열 위치; `LEFT`는 앞쪽 고정 길이.
- `SUM(PRICE*AMOUNT)` vs `SUM(AMOUNT)*PRICE`는 같은 그룹 내 가격이 일정할 때 분배법칙으로 동등. 실제 주문별 가격이 달라질 수 있다면 행별 곱을 합산해야 함.
- `YEAR(YM)`은 수치 연도, `DATE_FORMAT(YM,'%Y')`는 문자열 연도. 플랫폼의 출력 자료형·정렬 규칙에 주의.
- 출력용 `CONCAT(SUM(...),'km')`은 문자열이므로 이를 ORDER BY 하면 문자열 정렬. 숫자 `SUM(...)` 자체로 정렬해야 함.

## 서브쿼리와 그룹별 최댓값

- `FROM (SELECT...) AS alias`: 조회 결과를 테이블처럼 다루는 파생 테이블.
- `WHERE x IN (SELECT ...)`: 값이 결과 집합에 포함되는지. `EXISTS (SELECT 1 ...)`: 만족하는 행이 하나라도 있는지; `NOT EXISTS`는 없는지.
- `NOT IN`은 NULL 때문에 3값 논리 함정이 있을 수 있으니 주의.
- 상관 서브쿼리는 안쪽 WHERE에서 바깥쪽 테이블 별칭을 참조할 수 있음. 일반 FROM 파생 테이블은 같은 FROM의 이전 테이블을 직접 참조할 수 없고, MySQL 8.0.14+ `LATERAL`로 해결 가능.
- 그룹별 최고가 행 찾기 6가지 학습: MAX 파생 테이블과 원본 JOIN(그룹·가격 동시 매칭), 상관 스칼라 서브쿼리, 다중 컬럼 IN, NOT EXISTS, RANK, 자기 자신 LEFT JOIN.
- 최댓값 동점인 행은 여러 개일 수 있음. `RANK()`는 공동 1등을 모두 반환하지만 `ROW_NUMBER()`는 한 행만 선택할 수 있음.
- 164671 첫 서브쿼리 성공: `ORDER BY VIEWS DESC LIMIT 1`로 게시글 하나를 먼저 선택하고 그 게시글의 첨부파일 전체를 JOIN. 최종 JOIN 결과 뒤에서 LIMIT 1을 하면 파일을 하나만 출력할 수 있으므로 다른 문제.

## 윈도우 함수

- `OVER(PARTITION BY ... ORDER BY ...)`는 원본 행을 유지하며 합계/순위 계산.
- `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `NTILE(4)`의 동점·구간 처리 차이. `PARTITION BY`는 GROUP BY처럼 행을 합치지 않음.

## 학습·기록 원칙

1. 공식 프로그래머스 문제 풀이 전에는 답안 SQL 공개 금지. 오답이면 단계별 힌트 하나씩.
2. 통과 후 **다른 풀이 2~3개와 장단점**을 설명한다.
3. 매번 **남은 유형/문제 목록 전체**를 표시한다. 유형별 난이도 낮은 순으로 학습.
4. 사용자가 실제 제출한 SQL만 `solutions/`와 `attempts/`에 보존; 강의 예제는 이 노트와 분리.
5. 코드 검토 정답, 플랫폼 통과 보고, 오답, 미제출을 별도 상태로 보존.
6. 묶음 완료 시 GitHub 일괄 커밋. 명시적인 전체 학습 스냅샷 요청은 예외.
