def solution(str_list, ex):
    result=''
    for str in str_list:
        if ex in str: continue
        else: result+=str
    return result