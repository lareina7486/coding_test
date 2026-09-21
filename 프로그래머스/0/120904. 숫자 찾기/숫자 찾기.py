def solution(num, k):
    index=0
    for i in str(num):
        if int(i)==k:
            return index+1
        index+=1
    return -1