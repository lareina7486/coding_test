def solution(s):
    s_set=set(list(s))
    s=list(s)
    result=''
    for i in s_set:
        if s.count(i)==1:
            result+=i
    return ''.join(sorted(result))