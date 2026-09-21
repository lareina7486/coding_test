def solution(my_string):
    sum=0
    return len(list(map(int, filter(lambda x:x.isdigit(), my_string))))