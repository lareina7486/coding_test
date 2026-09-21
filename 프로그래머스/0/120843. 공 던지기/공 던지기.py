from collections import deque

def solution(numbers, k):
    d=deque(numbers)
    d.append(d.popleft())
    for i in range(k-1):
        d.append(d.popleft())
        d.append(d.popleft())
    return d[-1]
    