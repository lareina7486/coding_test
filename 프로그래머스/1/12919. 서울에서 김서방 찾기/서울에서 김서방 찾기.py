def solution(seoul):
    answer=-1
    for i in seoul:
        answer+=1
        if i == 'Kim':
            return f'김서방은 {answer}에 있다'