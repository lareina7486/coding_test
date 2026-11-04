# 2026-11-04 Lv.1·Lv.2 추가 실전 문제 풀이 기록

- 공식 출처: 프로그래머스 SQL 고득점 Kit (MySQL)
- 기존 CH01~CH04(31개)와 겹치지 않는 **신규 공식 문제 23개**를 도전함.
- **사용자가 작성한 최종 SQL 원문 22개**를 별도 파일로 저장. 대장균 1문제는 실제 작성/제출 코드가 없으므로 .sql 파일을 만들지 않음.
- 150문제 강제 목표 폐기, 필요한 문제 선택 학습.
- 상태는 '사이트 통과 보고', '코드 검토 적합', '미완료', '보완 권장'을 구분.
- 동일 문제의 수정 전 코드는 오답 메모로 기록하고, .sql에는 사용자가 실제 작성한 최신 코드를 저장.

## 문제 전체 목록

| 번호 | 실제 공식 문제 | 난이도 | 현재 상태 | SQL 파일 | 학습 개념 |
| ---: | --- | --- | --- | --- | --- |
| 1 | [가장 비싼 상품 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/131697) | Lv.1 | 코드 검토 정답 | [131697.sql](../solutions/programmers/131697.sql) | MAX |
| 2 | [조건에 맞는 회원수 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/131535) | Lv.1 | 코드 검토 정답 | [131535.sql](../solutions/programmers/131535.sql) | COUNT, 날짜 범위 |
| 3 | [과일로 만든 아이스크림 고르기](https://school.programmers.co.kr/learn/courses/30/lessons/133025) | Lv.1 | 첫 시도 정렬 오류 → 재풀이 코드 정답, 사이트 미확인 | [133025.sql](../solutions/programmers/133025.sql) | JOIN·정렬 |
| 4 | [잔챙이 잡은 수 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/293258) | Lv.1 | 코드 검토 정답 | [293258.sql](../solutions/programmers/293258.sql) | NULL |
| 5 | [Python 개발자 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/276013) | Lv.1 | 코드 검토 정답 | [276013.sql](../solutions/programmers/276013.sql) | OR / IN |
| 6 | [잡은 물고기 중 가장 큰 물고기의 길이 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/298515) | Lv.1 | 코드 검토 정답 | [298515.sql](../solutions/programmers/298515.sql) | MAX, CONCAT |
| 7 | [평균 일일 대여 요금 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/151136) | Lv.1 | 코드 검토 정답 | [151136.sql](../solutions/programmers/151136.sql) | AVG, ROUND |
| 8 | [잡은 물고기의 평균 길이 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/293259) | Lv.1 | 코드 검토 정답 | [293259.sql](../solutions/programmers/293259.sql) | IFNULL, AVG |
| 9 | [한 해에 잡은 물고기 수 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/298516) | Lv.1 | 코드 검토 정답 | [298516.sql](../solutions/programmers/298516.sql) | DATE/LIKE |
| 10 | [자동차 대여 기록에서 장기/단기 대여 구분하기](https://school.programmers.co.kr/learn/courses/30/lessons/151138) | Lv.1 | 미완료: 기간 계산 수정, DATE_FORMAT 출력 미수정 | [151138.sql](../solutions/programmers/151138.sql) | DATEDIFF, CASE, DATE_FORMAT |
| 11 | [가장 큰 물고기 10마리 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/298517) | Lv.1 | 코드 검토 정답 | [298517.sql](../solutions/programmers/298517.sql) | 복합 ORDER BY |
| 12 | [조건에 부합하는 중고거래 댓글 조회하기](https://school.programmers.co.kr/learn/courses/30/lessons/164673) | Lv.1 | 코드 검토 정답(날짜 표현은 플랫폼 확인 권장) | [164673.sql](../solutions/programmers/164673.sql) | JOIN, 날짜 형식 |
| 13 | [특정 형질을 가지는 대장균 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/301646) | Lv.1 | 풀이 보류·미제출 | 미제출 | 비트 AND, 비트마스크 |
| 14 | [DATETIME에서 DATE로 형 변환](https://school.programmers.co.kr/learn/courses/30/lessons/59414) | Lv.2 | 사용자 정답 통과 보고 | [59414.sql](../solutions/programmers/59414.sql) | DATE_FORMAT |
| 15 | [가격이 제일 비싼 식품의 정보 출력하기](https://school.programmers.co.kr/learn/courses/30/lessons/131115) | Lv.2 | 사용자 정답 통과 보고 | [131115.sql](../solutions/programmers/131115.sql) | ORDER BY, LIMIT |
| 16 | [조건에 맞는 아이템들의 가격의 총합 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/273709) | Lv.2 | 사용자 정답 통과 보고 | [273709.sql](../solutions/programmers/273709.sql) | SUM, WHERE |
| 17 | [카테고리 별 상품 개수 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/131529) | Lv.2 | 사용자 정답 통과 보고·정렬 구현 재검토 | [131529.sql](../solutions/programmers/131529.sql) | SUBSTR, GROUP BY |
| 18 | [중성화 여부 파악하기](https://school.programmers.co.kr/learn/courses/30/lessons/59409) | Lv.2 | 사용자 정답 통과 보고 | [59409.sql](../solutions/programmers/59409.sql) | CASE, LIKE |
| 19 | [진료과별 총 예약 횟수 출력하기](https://school.programmers.co.kr/learn/courses/30/lessons/132202) | Lv.2 | 사용자 정답 통과 보고 | [132202.sql](../solutions/programmers/132202.sql) | GROUP BY, COUNT |
| 20 | [자동차 종류 별 특정 옵션이 포함된 자동차 수 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/151137) | Lv.2 | 코드 검토 정답 | [151137.sql](../solutions/programmers/151137.sql) | OR, GROUP BY |
| 21 | [입양 시각 구하기(1)](https://school.programmers.co.kr/learn/courses/30/lessons/59412) | Lv.2 | 오답 재풀이 → 코드 검토 정답, 사이트 미채점 | [59412.sql](../solutions/programmers/59412.sql) | HOUR, WHERE, BETWEEN, GROUP BY |
| 22 | [성분으로 구분한 아이스크림 총 주문량](https://school.programmers.co.kr/learn/courses/30/lessons/133026) | Lv.2 | 코드 검토: 집계 적합·LEFT JOIN 매칭 가정 확인 | [133026.sql](../solutions/programmers/133026.sql) | JOIN, GROUP BY, SUM |
| 23 | [3월에 태어난 여성 회원 목록 출력하기](https://school.programmers.co.kr/learn/courses/30/lessons/131120) | Lv.2 | 조건·정렬 적합·날짜 출력 형식 보완 권장, 사이트 미채점 | [131120.sql](../solutions/programmers/131120.sql) | MONTH, IS NOT NULL, DATE_FORMAT |

## 주요 오답·보완 사항

### 과일로 만든 아이스크림 고르기

첫 시도 ORDER BY TOTAL_ORDER ASC가 오류였음. 오른쪽 테이블 필터 때문에 LEFT JOIN이 사실상 INNER JOIN 역할.

### Python 개발자 찾기

대안: WHERE 'Python' IN (SKILL_1, SKILL_2, SKILL_3)

### 한 해에 잡은 물고기 수 구하기

DATE 컬럼에는 연도 범위 조건도 학습 권장.

### 자동차 대여 기록에서 장기/단기 대여 구분하기

수정 전에는 END_DATE-START_DATE로 계산했음. 최신 제출은 일수 계산을 고쳤으나 날짜 출력 형식 미보완.

### 조건에 부합하는 중고거래 댓글 조회하기

날짜 출력 형식을 요구하므로 DATE_FORMAT 및 ORDER BY reply.CREATED_DATE 등 명시적 한정 재점검.

### 특정 형질을 가지는 대장균 찾기

사용자 요청: 이후 비트 연산 단계에서 학습.

### 카테고리 별 상품 개수 구하기

공식 요구 정렬은 CATEGORY 오름차순. ORDER BY PRODUCT_CODE는 그룹화 이후 비집계 열 정렬이므로 비결정적이거나 ONLY_FULL_GROUP_BY 에러 위험. ORDER BY CATEGORY 권장.

### 중성화 여부 파악하기

다른 풀이: IF(SEX_UPON_INTAKE REGEXP 'Neutered|Spayed','O','X')

### 진료과별 총 예약 횟수 출력하기

전체 COUNT와 진료과별 GROUP BY COUNT 차이 보충 학습 완료.

### 자동차 종류 별 특정 옵션이 포함된 자동차 수 구하기

대안: REGEXP '통풍시트|열선시트|가죽시트' 또는 INSTR.

### 입양 시각 구하기(1)

최초 WHERE HOUR 별칭 참조 + OR 범위 오류. WHERE HOUR(DATETIME) >= 9 AND HOUR(DATETIME) <= 19도 맞음.

### 성분으로 구분한 아이스크림 총 주문량

공식 스키마에는 ICECREAM_INFO.FLAVOR → FIRST_HALF.FLAVOR 외래 키만 명시. FIRST_HALF의 모든 맛이 ICECREAM_INFO에도 존재하는지 별도 보장이 없어 INNER JOIN이 의미상 더 안전.

### 3월에 태어난 여성 회원 목록 출력하기

공식 주의사항: 날짜 표시 예시 YYYY-MM-DD 필수. DATE_FORMAT(DATE_OF_BIRTH,'%Y-%m-%d') AS DATE_OF_BIRTH로 명시 권장.


## 오늘 전체 학습에서 중요한 개념

1. **WHERE와 HAVING**: 원본 행 필터 vs 집계 그룹 필터.
2. **SELECT 별칭**은 MySQL `ORDER BY`/`GROUP BY`에서 참조할 수 있지만 `WHERE`에서는 참조 불가.
3. **GROUP BY**: 전체 COUNT vs 카테고리/진료과/시간대별 COUNT.
4. **INNER/LEFT/RIGHT OUTER JOIN**과 anti-join 패턴. OUTER JOIN 뒤 WHERE가 NULL 보존을 무효화할 수 있음.
5. `DATE_FORMAT`, `HOUR`, `MONTH`, `DATEDIFF`, `BETWEEN`의 사용 위치·출력 규칙.
6. `CASE` / `IF` / `REGEXP` / `INSTR` 같은 대안 문법.
7. `ORDER BY`에 실제 요구된 열·방향·동률 처리 규칙을 빠짐없이 지정.
8. SQL 실행 성공과 공식 출력 형식 만족, 실제 플랫폼 통과는 구별해야 함.

## 다음 복습 우선순위

1. 자동차 장기/단기: DATE_FORMAT 두 컬럼 출력, 일수 포함 계산, CASE.
2. 3월 여성 회원: DATE_OF_BIRTH 명시적 날짜 서식.
3. 카테고리별 상품: 집계 기준과 ORDER BY 기준을 일치.
4. CH01 09 다중 정렬 재제출.
5. 비트 연산 사전 학습 후 대장균.
6. CH05 서브쿼리 문제 본격 제출.

**실제 실행·검증은 하지 않았습니다.** 최종 SQL 원문/학습 이력은 사용자 제공 내용 기반입니다.
