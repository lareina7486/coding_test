# coding_test

코딩테스트 문제 풀이와 기본 알고리즘 패턴을 복습하는 개인 학습 저장소입니다.

## 저장소 구성

| 경로 | 내용 |
| --- | --- |
| [프로그래머스/0](프로그래머스/0) | 프로그래머스 Lv.0 풀이 모음 |
| [프로그래머스/1](프로그래머스/1) | 프로그래머스 Lv.1 풀이 모음 |
| [프로그래머스/2](프로그래머스/2) | 프로그래머스 Lv.2 풀이 모음 |
| [practice/python/algorithm_patterns.py](practice/python/algorithm_patterns.py) | 해시·이진 탐색·슬라이딩 윈도 예제와 자체 테스트 |
| [docs/WRONG_ANSWER_LOG.md](docs/WRONG_ANSWER_LOG.md) | 오답 원인·최소 반례·재검증을 기록하는 템플릿 |

`프로그래머스` 디렉터리는 기존 문제 풀이 기록이며, `practice` 디렉터리는 별도의 학습 예제입니다. 연습 예제를 온라인 저지에 제출·통과한 풀이로 표현하지 않습니다.

## Python 기본 패턴 직접 검증

Python 3.9 이상 환경에서 다음처럼 실행합니다.

```bash
python3 practice/python/algorithm_patterns.py -v
```

현재 예제는 합이 목표값인 두 수 찾기, lower bound(하한 이진 탐색), 중복 없는 최장 부분 문자열을 다룹니다. 각 예제에는 일반·경계 입력을 검사하는 `unittest` 테스트가 포함되어 있습니다.

## 복습 원칙

- 정답만 저장하지 않고 **실패한 가정과 최소 반례**를 기록합니다.
- 정렬 여부, 빈 입력, 중복값과 시간 복잡도를 다시 확인합니다.
- 실제로 수행한 테스트만 검증 완료로 기록합니다.

---

초기 README는 [BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub) 자동 푸시 저장소 안내로 만들어졌으며, 위 목차는 현재 저장소 파일 구성에 맞춰 정리했습니다.
