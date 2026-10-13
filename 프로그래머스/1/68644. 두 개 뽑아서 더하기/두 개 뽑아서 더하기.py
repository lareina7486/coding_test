from itertools import combinations

def solution(numbers):
    return sorted(set(sum(group) for group in combinations(numbers,2)))
        