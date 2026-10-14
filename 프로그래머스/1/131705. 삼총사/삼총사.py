def solution(number):
    count=0
    answer=[]
    
    def dfs(depth, start):
        nonlocal count
        
        if depth==3:
            if sum(answer)==0:
                count+=1
            return
        
        for i in range(start, len(number)):
            answer.append(number[i])
            dfs(depth+1, i+1)
            answer.pop()
        
    dfs(0, 0)
    return count
    