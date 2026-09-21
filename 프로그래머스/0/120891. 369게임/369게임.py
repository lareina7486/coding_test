def solution(order):
    clap=['3','6','9']
    count=0
    for i in str(order):
        if i in clap: count+=1
    return count