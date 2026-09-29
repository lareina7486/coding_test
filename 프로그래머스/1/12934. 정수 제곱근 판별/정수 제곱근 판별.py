def solution(n):
    x = 1
    while x**2 <= n:
        if x**2 == n:
            return (x+1)**2
        x += 1
    return -1