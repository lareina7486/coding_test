# CH06 · GROUP BY / JOIN 심화 (2026-11-06 이후)

| 문제 | 사용자 보고 상태 | 원문 |
|---|---|---|
| [131530 가격대 별 상품 개수](https://school.programmers.co.kr/learn/courses/30/lessons/131530) | 플랫폼 통과 | [131530.sql](../solutions/programmers/131530.sql) |
| [144855 카테고리 별 도서 판매량](https://school.programmers.co.kr/learn/courses/30/lessons/144855) | 플랫폼 통과 · 현재 전체 SQL 원문 미확인 | 상태만 보관 |
| [164668 조건에 맞는 사용자와 총 거래금액](https://school.programmers.co.kr/learn/courses/30/lessons/164668) | 플랫폼 통과 · 현재 전체 SQL 원문 미확인 | 상태만 보관 |
| [157340 대여 중/대여 가능](https://school.programmers.co.kr/learn/courses/30/lessons/157340) | 오답 재도전 후 플랫폼 통과 | [157340.sql](../solutions/programmers/157340.sql) · [2그룹 상세](remaining-32-group-02-date-period.md) |
| [144856 저자별 카테고리별 매출액](https://school.programmers.co.kr/learn/courses/30/lessons/144856) | 미제출·보류 | 없음 |

### 배운 문법과 비교

- 가격대 그룹: `PRICE DIV 10000`, `FLOOR(PRICE/10000)`, `TRUNCATE(PRICE,-4)`, `PRICE-MOD(PRICE,10000)` (비음수 가격 기준).
- 월 조회: `YEAR(date)=2022 AND MONTH(date)=1`, `DATE_FORMAT`, `date >= '2022-01-01' AND date < '2022-02-01'`. 일반적인 날짜 인덱스 사용에 범위 검색이 유리할 수 있음.
- `WHERE`는 집계 전 데이터 필터, `HAVING`은 GROUP BY 이후 집계 필터.
- 164668은 DONE 거래만 선택한 뒤 사용자별 합계·`HAVING TOTAL_SALES>=700000`; 금액 오름차순 정렬.
- `MAX(END_DATE)`만으로 기준일 당시 대여 중 여부를 판단할 수 없음. 기준일이 실제 START_DATE~END_DATE 안에 포함되는 대여가 있는지 검사.
- 사용자 SQL을 직접 확인하지 못한 문제의 모범 SQL은 만들어서 원문 파일로 저장하지 않음.
