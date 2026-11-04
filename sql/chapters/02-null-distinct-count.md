# CH02 — NULL · 중복 제거 · COUNT (1회독 완료)

- 학습일: 2026-11-04
- DB: MySQL (프로그래머스 SQL 고득점 Kit)
- 학습 문제: 공식 문제 16~21번 6개
- 코딩 내용: 사용자 본인이 대화에서 제출한 SQL 원문 보관
- 처리 상태: SQL 코드 검토 6/6 적합. **플랫폼 정답 통과 보고**: 16, 20(재풀이), 21. **코드 검토만 완료·플랫폼 채점 미확인**: 17, 18, 19.
- 실제 소요 시간: 미기록 (추정하지 않음)

## 배운 핵심 개념

- `IS NULL` / `IS NOT NULL`: NULL 값 검사. `= NULL`은 사용하지 않음.
- `IFNULL(value, fallback)`: NULL을 대체값으로 변경. `COALESCE`는 여러 후보를 순차 확인.
- `COUNT(*)`: 모든 행 수. `COUNT(column)`: 해당 컬럼에서 NULL 아닌 값 수.
- `COUNT(DISTINCT column)`: NULL과 중복을 제거한 서로 다른 값 수.
- `LIKE '경기도%'`: 지정한 접두어로 시작하는 문자열 조건.
- `AS`: 표현식의 결과 컬럼 이름 지정.

## 공식 문제·작성 코드

| 번호 | 공식 문제 | 문제 링크 | SQL 파일 | 확인 상태 |
| ---: | --- | --- | --- | --- |
| 16 | 이름이 없는 동물의 아이디 | [59039](https://school.programmers.co.kr/learn/courses/30/lessons/59039) | [59039.sql](../solutions/programmers/59039.sql) | 플랫폼 통과 보고 |
| 17 | 이름이 있는 동물의 아이디 | [59407](https://school.programmers.co.kr/learn/courses/30/lessons/59407) | [59407.sql](../solutions/programmers/59407.sql) | 코드 검토 정답, 플랫폼 미채점 |
| 18 | NULL 처리하기 | [59410](https://school.programmers.co.kr/learn/courses/30/lessons/59410) | [59410.sql](../solutions/programmers/59410.sql) | 코드 검토 정답, 플랫폼 미채점 |
| 19 | 경기도에 위치한 식품창고 목록 출력하기 | [131114](https://school.programmers.co.kr/learn/courses/30/lessons/131114) | [131114.sql](../solutions/programmers/131114.sql) | 코드 검토 정답, 플랫폼 미채점 |
| 20 | 나이 정보가 없는 회원 수 구하기 | [131528](https://school.programmers.co.kr/learn/courses/30/lessons/131528) | [131528.sql](../solutions/programmers/131528.sql) | 최초 오답 → 정답 통과 보고 |
| 21 | 중복 제거하기 | [59408](https://school.programmers.co.kr/learn/courses/30/lessons/59408) | [59408.sql](../solutions/programmers/59408.sql) | 플랫폼 통과 보고 |

## 오답 분석 — 20번

**최초 코드(오답):**

```sql
SELECT COUNT(AGE IS NULL) AS USERS
FROM USER_INFO;
```

`AGE IS NULL`은 MySQL에서 참일 때 1, 거짓일 때 0이므로 `COUNT(표현식)`이 둘 다 셉니다. 즉 나이가 있는 회원까지 포함한 행 수를 구합니다.

**사용자 재작성 후 통과 보고한 SQL:**

```sql
SELECT COUNT(*) AS USERS
FROM USER_INFO
WHERE AGE IS NULL;
```

`WHERE`로 NULL 행만 남기고 `COUNT(*)`를 적용합니다. 2회독에서 `COUNT(*)`, `COUNT(컬럼)`, `COUNT(DISTINCT 컬럼)` 차이를 복습할 것.

## 개선 포인트 — 19번

사용자 SQL은 `IFNULL(FREEZER_YN, 'N')`으로 맞는 값을 계산합니다. 결과 컬럼 이름을 명확히 하고 싶다면 `AS FREEZER_YN`을 추가할 수 있으나, **보관 SQL 파일에는 사용자가 작성한 원문을 유지**했습니다.

## 챕터 완료 판정

- 기본 NULL 조회·대체·중복 제거·COUNT 활용을 모두 경험했습니다.
- 20번 오답 수정까지 완료하여 CH02 1회독을 종료합니다.
- CH03의 22~26번은 **별도 챕터**입니다. 25·26은 아직 미풀이이며 이 기록에 포함하지 않았습니다.
