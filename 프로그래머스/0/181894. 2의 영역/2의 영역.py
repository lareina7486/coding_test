def solution(arr):
    l=[]
    for i in range(len(arr)):
        if arr[i]==2:
            l.append(i)
    if not l: return [-1]
    else:
        return arr[l[0]:l[-1]+1]
        