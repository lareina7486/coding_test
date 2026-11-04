# CH03 — 집계함수 · GROUP BY · HAVING (1회독 완료: 코드 검토 기준)

- 학습일: 2026-11-04
- DB: MySQL (프로그래머스 SQL 고득점 Kit)
- 신규 문제: 22~26번, 총 **5개**
- CH02의 20번 재풀이와 구분하여 집계
- 직접 작성한 SQL을 저장. 사이트 정답 판정 여부와 SQL 내용 검토 결과를 구분
- 실제 학습 시간: 보고되지 않음

## 실제 공식 문제 및 상태

| 번호 | 공식 문제 | 링크 | 풀이 파일 | 검토 결과 / 플랫폼 상태 |
| ---: | --- | --- | --- | --- |
| 22 | 최댓값 구하기 | [59415](https://school.programmers.co.kr/learn/courses/30/lessons/59415) | [59415.sql](../solutions/programmers/59415.sql) | 코드 적합; 사이트 정답 통과 보고 (2가지 방식 작성) |
| 23 | 최솟값 구하기 | [59038](https://school.programmers.co.kr/learn/courses/30/lessons/59038) | [59038.sql](../solutions/programmers/59038.sql) | 코드 적합; 사이트 미채점 보고 |
| 24 | 동물 수 구하기 | [59406](https://school.programmers.co.kr/learn/courses/30/lessons/59406) | [59406.sql](../solutions/programmers/59406.sql) | 코드 적합; 사이트 미채점 보고 |
| 25 | 고양이와 개는 몇 마리 있을까 | [59040](https://school.programmers.co.kr/learn/courses/30/lessons/59040) | [59040.sql](../solutions/programmers/59040.sql) | 첫 제출 미완성 → 재풀이 코드 적합, 사이트 상태 unknown |
| 26 | 동명 동물 수 찾기 | [59041](https://school.programmers.co.kr/learn/courses/30/lessons/59041) | [59041.sql](../solutions/programmers/59041.sql) | 첫 제출 미완성 → 재풀이 코드 적합, 사이트 상태 unknown |

> **판정 기준**: 22~26번의 현재 SQL은 공식 문제 요구사항과 MySQL 문법상 일치합니다. 단, 25·26번은 실제 온라인 채점 완료를 확인하지 않았으므로 '플랫폼 통과'로 기록하지 않습니다.

## 핵심 개념

- `MAX()` / `MIN()`: 최대·최솟값 구하기
- `COUNT(*)`: 행 수 세기 (행의 값이 NULL이라도 포함)
- `GROUP BY col`: 같은 값끼리 그룹 생성; 일반 컬럼은 그룹 기준 또는 함수 종속성을 지켜야 함
- `HAVING COUNT(*) > 1`: 그룹화 이후 그룹에 조건 적용
- `WHERE`: 그룹화 전에 개별 행 필터
- `ORDER BY`: 결과 표시 순서 지정; `GROUP BY`만으로는 결과 순서 보장 안 됨
- `SELECT COUNT(*) AS COUNT ... HAVING COUNT > 1`: MySQL은 집계 결과에 붙인 **SELECT 별칭**을 HAVING에서 참조하도록 허용. 가독성/이식성을 위해 `HAVING COUNT(*) > 1`도 기억.
- 논리적 처리 순서: `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT`. DB 엔진의 실제 물리적 실행 순서와 다르며, MySQL 별칭 참조는 논리적 순서에 대한 단순한 설명의 예외처럼 보일 수 있음.

## 25번 오답 → 수정

첫 코드:

```sql
SELECT ANIMAL_TYPE, COUNT(*) AS count
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE;
```

그룹별 계산은 정확했으나 문제에서 요구하는 **고양이 우선 정렬**이 빠짐.

사용자가 재작성한 SQL:

```sql
SELECT ANIMAL_TYPE, COUNT(*) AS count
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE;
```

## 26번 오답 → 수정

첫 코드:

```sql
SELECT NAME, COUNT(*) AS COUNT
FROM ANIMAL_INS
GROUP BY NAME;
```

**이름 NULL 제외**, **두 번 이상 쓰인 이름 선별**, **이름 오름차순 정렬** 조건이 빠짐.

사용자가 재작성한 SQL:

```sql
SELECT NAME, COUNT(*) AS COUNT
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
GROUP BY NAME
HAVING COUNT > 1
ORDER BY NAME;
```

MySQL에서 `COUNT`는 `SELECT`의 별칭으로 해석할 수 있음. 다른 SQL 방언과의 호환성을 고려할 때 `HAVING COUNT(*) > 1` 권장.

## 22번 두 가지 풀이의 차이

`MAX(DATETIME)`은 집계값을 계산합니다. `ORDER BY DATETIME DESC LIMIT 1`은 최댓값이 있는 실제 행 하나를 조회합니다. 테이블이 비어 있으면 전자는 NULL 결과 행 하나를 반환하지만, 후자는 반환 행이 없습니다.

## 다음 복습 시점

- 25번: GROUP BY 뒤 정렬 필수 여부를 원문 조건에서 확인하는 습관
- 26번: WHERE(행) / HAVING(그룹) / ORDER BY(결과)의 역할 구분
- 사이트 채점 상태 미확인 문제(23~26)를 나중에 재확인하고, 정답 판정 시 학습 기록에 반영

## 완료 판단

현재 5개 문제 모두 SQL 코드의 논리와 공식 요구사항을 검토했으며, 미완성 2개를 재작성했습니다. CH03은 **학습상 완료**로 기록하지만, 실제 사이트 검증은 별도 상태로 유지합니다.
