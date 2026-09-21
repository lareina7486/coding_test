def solution(my_string):
    n=-len(my_string)
    suffix=[]
    for i in range(len(my_string)):
        suffix.append(my_string[n:])
        n+=1
    return sorted(suffix)