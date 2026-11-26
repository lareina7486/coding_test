def solution(s):
    list = [0,0]
    count=0
    target=''
    
    for ch in s:
        if not target:
            target=ch
            list[0]+=1
        elif ch==target:
            list[0]+=1
        else:
            list[1]+=1
        
        if list[0]==list[1]:
            count+=1
            list=[0,0]
            target=''
        
    if list!=[0,0]:
        count+=1
    
    return count