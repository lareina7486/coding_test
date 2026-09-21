def solution(numLog):
    answer=''
    key=dict(zip([1,-1,10,-10], ['w','s','d','a']))
    for i in range(len(numLog)-1):
        num=numLog[i+1]-numLog[i]
        answer+=key[num]
    return answer
            