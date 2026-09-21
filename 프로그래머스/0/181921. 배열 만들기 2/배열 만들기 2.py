def solution(l, r):
    arr=[]
    a=''
    for i in range(l,r+1):
        if str(i).replace('5','').replace('0','')=='':
            arr.append(i)
    return arr if arr else [-1]