from itertools import combinations

def solution(number):
    return sum([sum(group)==0 for group in combinations(number,3)])