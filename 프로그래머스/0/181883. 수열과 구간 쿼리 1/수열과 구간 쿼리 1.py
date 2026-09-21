def solution(arr, queries):
    for s,e in queries:
        for j in range(s,e+1):
            arr[j]+=1
    return arr