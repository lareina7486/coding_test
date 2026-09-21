def solution(n, k):
    result=[k]
    i=2
    while n>=k*i:
        result.append(k*i)
        i+=1
    return result