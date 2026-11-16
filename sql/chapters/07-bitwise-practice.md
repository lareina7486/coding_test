# CH07 — 비트 연산·조건 분류

2026-11-16 기준 사용자 제출 및 학습 이력. **플랫폼 통과와 SQL 원문 확인 여부를 분리**한다.

| 문제 | 상태 | 실제 작성된 SQL |
|---|---|---|
| [299307 대장균의 크기에 따라 분류하기 1](https://school.programmers.co.kr/learn/courses/30/lessons/299307) | 사용자 플랫폼 통과 보고 | [299307.sql](../solutions/programmers/299307.sql) |
| [301646 특정 형질을 가지는 대장균 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/301646) | 2회 오답 후 사용자가 최종 '풀어서 통과' 보고, **최종 SQL 원문 미제공** | [1차 오답](../attempts/programmers/301646-first.sql), [2차 오답](../attempts/programmers/301646-second.sql) |
| [276034 조건에 맞는 개발자 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/276034) | **오답·보류**, 힌트 받고 더 고민하기로 함 | [276034-initial.sql](../attempts/programmers/276034-initial.sql) |
| [301647 부모의 형질을 모두 가지는 대장균 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/301647) | **미제출·보류** | 없음 |
| [276035 FrontEnd 개발자 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/276035) | 미제출 | 없음 |
| [276036 언어별 개발자 분류하기](https://school.programmers.co.kr/learn/courses/30/lessons/276036) | 미제출 | 없음 |

## 핵심 배운 내용

- 비트마스크 n번째 특성은 `2^(n-1)`이므로 1번=1, 2번=2, 3번=4, 4번=8이다.
- `BIN(x)`는 숫자의 이진수 형태 **문자열**을 반환하므로 `&`에서 그대로 쓰면 의도치 않은 변환을 초래할 수 있다. 비트 AND는 정수형으로 사용.
- 301646 최초 SQL은 `BIN()`을 사용했고, 두 번째는 `GENOTYPE & 3`을 3번 형질 마스크로 착각했다. 이후 사용자 사이트 통과 **보고만** 있어 최종 SQL은 미복원.
- 276034 `dev.SKILL_CODE = skill.CODE`는 개발자 스킬이 여러 비트 합성값일 때 잘못된 JOIN 조건. 포함된 스킬 비트를 검사해야 함. **미해결**.
- 301647은 부모/자식의 비트마스크 포함 관계와 SELF JOIN 학습 대상. **SQL 미제출**.
- 299307은 `CASE WHEN SIZE_OF_COLONY<=100 THEN 'LOW' WHEN <=1000 THEN 'MEDIUM' ELSE 'HIGH'` 사용. 실제 사용자 SQL 원문 유지. 정렬 여부 개선안이 있더라도 임의 수정하지 않는다.
