def solution(s):
    arr = [4,6]
    answer = True
    if len(s) in arr: # 48~57
        for i in s:
            if ord(i)>57:
                answer = False
        return answer
    else:
        return False