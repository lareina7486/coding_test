def solution(s):
    balance=0
    count=0
    target=''
    
    for ch in s:
        if not target:
            target=ch
            balance+=1
        elif ch==target:
            balance+=1
        else:
            balance-=1
        
        if balance==0:
            count+=1
            balance=0
            target=''
        
    if balance!=0:
        count+=1
    
    return count