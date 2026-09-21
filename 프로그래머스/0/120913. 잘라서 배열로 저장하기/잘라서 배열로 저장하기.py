import math
def solution(my_str, n):
    result=[]
    for i in range(math.ceil(len(my_str)/n)):
        result.append(my_str[i*n:(i+1)*n])
    return result