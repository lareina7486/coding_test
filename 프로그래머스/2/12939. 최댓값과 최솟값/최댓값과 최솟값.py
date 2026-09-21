def solution(s):
    s_list=s.split(' ')
    
    max_num = float('-inf')
    min_num = float('inf')
    
    for num in s_list:
        num=int(num)
        if num>max_num:
            max_num=num
            
        if num<min_num:
            min_num=num
    
    return str(min_num)+' '+str(max_num)