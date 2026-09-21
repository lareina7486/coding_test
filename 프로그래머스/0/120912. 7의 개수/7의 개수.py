def solution(array):
    count=0
    s=''.join(str(array))
    for i in s:
        if i=='7': count+=1
    return count