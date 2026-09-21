def solution(i, j, k):
    result=0
    for a in range(i,j+1):
        if str(k) in str(a):
            c=str(a).count(str(k))
            result+=c
    return result