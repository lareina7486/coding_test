def solution(price, money, count):
    c = sum([price*i for i in range(1,count+1)])-money
    return c if c>0 else 0