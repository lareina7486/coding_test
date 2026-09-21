def solution(intStrs, k, s, l):
    arr=[]
    for i in intStrs:
        z=int(i[s:s+l])
        if z>k: arr.append(z)
    return arr