from itertools import combinations

def solution(number):
    count=0
    result=list(combinations(number,3))
    for a,b,c in result:
        if a+b+c==0: count+=1
    return count