def solution(order):
    sum=0
    for menu in order:
        if 'latte' in menu: sum+=5000
        else: sum+=4500
    return sum
            