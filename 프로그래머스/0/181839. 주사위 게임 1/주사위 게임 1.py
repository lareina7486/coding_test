def solution(a, b):
    if (a+b)%2: return 2*a+2*b
    else: return a*a+b*b if a%2 else abs(a-b)