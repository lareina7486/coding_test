def solution(s1, s2):
    s=[]
    s=s1+s2
    return len(s1)+len(s2)-len(set(s))