def solution(array):
    arr=[]
    s=set(array)
    for i in s:
        arr.append(array.count(i))
    if arr.count(max(arr))>1:
        return -1
    else:
        s=list(s)
        return s[arr.index(max(arr))]