from collections import deque

def solution(A, B):
    queue=deque(A)
    for i in range(len(A)):
        if ''.join(queue)==B:
            return i
        queue.appendleft(queue.pop())
    return -1