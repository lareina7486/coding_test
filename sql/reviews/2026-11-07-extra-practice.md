# 2026-11-07 추가 SQL 실전 — 개별 기록 요청

## 완료한 공식 문제

- **문제:** [부서별 평균 연봉 조회하기](https://school.programmers.co.kr/learn/courses/30/lessons/284529) (Lv.3)
- **플랫폼:** 사용자가 프로그래머스에서 정답 통과했다고 보고함
- **체감 난이도:** 쉬움
- **사용자 직접 작성한 SQL:** [284529.sql](../solutions/programmers/284529.sql)
- **개념:** HR_DEPARTMENT↔HR_EMPLOYEES INNER JOIN, 부서별 GROUP BY, AVG(SAL), ROUND(...,0), AVG_SAL DESC
- **판정:** 공식 문제 요구사항과 코드 대조 적합. 플랫폼 실행은 직접 하지 않았으며 사용자 정답 보고를 기록함.

## 학습 중인 공식 문제 (미제출)

- [즐겨찾기가 가장 많은 식당 정보 출력하기](https://school.programmers.co.kr/learn/courses/30/lessons/131123): 사용자가 `GROUP BY FOOD_TYPE`과 `MAX(FAVORITES)`만으로는 `REST_ID`·`REST_NAME`을 올바르게 고를 수 없다는 점을 인지. 파생 테이블/서브쿼리에서 음식 종류별 최고 즐겨찾기를 구한 후 원본 REST_INFO와 FOOD_TYPE·FAVORITES 두 조건으로 매칭하는 개념 학습 중. **정답 SQL 미제출**.
- 다른 보류 문제 157340, 144856, 301647, 276034 및 미제출 133027은 사용자 요청대로 보류 유지. 이전 문제 원문은 이번 커밋에 추가하지 않음.
