def solution(s):
    arr = s.split(' ')
    answer = []
    
    for text in arr:
        for i, alpha in enumerate(list(text)):
            if i%2==0:
                answer.append(alpha.upper())
            else:
                answer.append(alpha.lower())
        answer.append(' ')
    
    return ''.join(answer[:-1])