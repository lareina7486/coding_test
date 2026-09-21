def solution(s):
    list = [0,0]
    ch=''
    cnt=0
    
    for i, j in enumerate(s):
        if i==0:
            ch=j
            list[0]+=1
            continue
        else:
            if j==ch: list[0]+=1
            else: list[1]+=1
    
        if list[0]==list[1]:
            cnt+=1
            list=[0,0]
            if i!=len(s)-1:
                ch=s[i+1]
            else:
                ch=''
            
    # 마지막 남은 문자 처리
    if list != [0, 0]:
        cnt += 1
    
    return cnt