def solution(number):
    count=0
    answer=[]
    path=[]
    
    def dfs(depth, start):
        nonlocal count
        
        if depth==3 :
            if sum(answer)==0:
                count+=1
            return
        
        for i in range(start, len(number)):
            path.append(i)
            answer.append(number[i])
            dfs(depth+1, start+1)
            path.pop()
        
    return dfs(0, 0)
    