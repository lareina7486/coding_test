def solution(arr):
    list=[]
    for i in arr:
        if i>=50 and i%2==0:
            list.append(i/2)
        elif i<50 and i%2:
            list.append(i*2)
        else: list.append(i)
    return list