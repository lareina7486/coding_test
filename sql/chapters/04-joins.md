# CH04 — JOIN 기초 완료

- 학습일: 2026-11-04
- MySQL / 프로그래머스 SQL 고득점 Kit
- 신규 문제 5개(27~31). 사용자 작성 SQL 원문은 `../solutions/programmers/`에서 확인.
- 수행시간은 미기록. **문제 코드 검토**와 **프로그래머스 통과 보고**를 구별합니다.
- 챕터 완료 기준: 27~31번 최종 SQL을 공식 문제 조건과 비교해 적합하다고 판단. 31번은 사용자가 실제 정답 통과(pass)를 보고함.

## 공식 문제별 기록

| 번호 | 공식 문제 및 링크 | 사용자 SQL | 결과 |
| ---: | --- | --- | --- |
| 27 | [조건에 맞는 도서와 저자 리스트 출력하기](https://school.programmers.co.kr/learn/courses/30/lessons/144854) | [144854.sql](../solutions/programmers/144854.sql) | 사용자 pass 보고 · 코드 검토 적합 |
| 28 | [상품 별 오프라인 매출 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/131533) | [131533.sql](../solutions/programmers/131533.sql) | 사용자 pass 보고 · 코드 검토 적합 |
| 29 | [없어진 기록 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/59042) | [59042.sql](../solutions/programmers/59042.sql) | 코드 검토 적합 · 플랫폼 미채점 |
| 30 | [오랜 기간 보호한 동물(1)](https://school.programmers.co.kr/learn/courses/30/lessons/59044) | [59044.sql](../solutions/programmers/59044.sql) | 코드 검토 적합 · 플랫폼 미채점 |
| 31 | [있었는데요 없었습니다](https://school.programmers.co.kr/learn/courses/30/lessons/59043) | [59043.sql](../solutions/programmers/59043.sql) | 처음 오류 → 수정 후 사용자 pass 보고 |

## 핵심 개념

- `INNER JOIN`: 연결 조건에 일치하는 행
- `LEFT JOIN` / `LEFT OUTER JOIN`: 왼쪽 테이블의 행 유지, 매칭 실패 시 오른쪽 열 NULL
- `RIGHT JOIN` / `RIGHT OUTER JOIN`: 오른쪽 테이블의 행 유지, 매칭 실패 시 왼쪽 열 NULL
- **Anti Join 패턴**: OUTER JOIN으로 유지한 행 중 상대편 키가 NULL인 행만 추출 (`WHERE 상대편.ID IS NULL`).
- JOIN 키가 각 테이블에서 유일한지 확인. 일대다 JOIN 시 행 증가 가능.
- 여러 테이블에 같은 이름의 열(`DATETIME`, `ANIMAL_ID` 등)이 존재하면 `테이블명.컬럼` 또는 테이블 별칭(`I.DATETIME`)을 명시.
- `INNER JOIN`과 함께 `WHERE I.DATETIME > O.DATETIME`으로 입소일/입양일 등 날짜 비교 가능.
- `JOIN + GROUP BY + SUM(PRICE * SALES_AMOUNT)`: 연결한 판매 데이터 집계.
- `ORDER BY`에서는 SELECT 출력 열이 우선 해석될 수 있지만 명시적 테이블 한정이 안전.

## 오답 및 개선 사항

### 29번 — 매칭되지 않은 쪽에서 조회하려던 초기 실수

첫 시도는 `RIGHT JOIN` 후 `ANIMAL_INS.ANIMAL_ID`, `ANIMAL_INS.NAME`을 선택하여 NULL이 될 문제. 사용자 스스로 `ANIMAL_OUTS`의 열을 선택하도록 수정. 보존할 테이블에서 출력하고, **매칭되지 않는 테이블**에서 `IS NULL` 검사.

### 31번 — 모호한 DATETIME 정렬

최초 작성:

```sql
SELECT ANIMAL_INS.ANIMAL_ID, ANIMAL_INS.NAME
FROM ANIMAL_INS
INNER JOIN ANIMAL_OUTS
    ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
WHERE ANIMAL_INS.DATETIME > ANIMAL_OUTS.DATETIME
ORDER BY DATETIME;
```

날짜 비교는 맞지만, `DATETIME` 열이 두 테이블에 모두 있으므로 `ORDER BY DATETIME`이 모호함.

최종 작성 SQL은 `ORDER BY ANIMAL_INS.DATETIME;`으로 수정했고, 프로그래머스 **pass** 보고함. SQL 원문은 위 59043.sql에 저장.

## 2회독 때 복습

1. `INNER` / `LEFT OUTER` / `RIGHT OUTER` 각각의 보존 행 구분
2. 미매칭 행 찾기(anti join), NULL 검사 대상 및 SELECT 출처 결정
3. JOIN 결과 행 수와 중복, `ON` vs `WHERE` 위치
4. 날짜 비교와 동일한 컬럼명 모호성 해결
5. 29, 30번 플랫폼 정답 통과 여부 별도 확인

## 다음 챕터

CH05 서브쿼리(`IN`, `EXISTS`, `NOT EXISTS`, 스칼라·상관 서브쿼리) 입문.
