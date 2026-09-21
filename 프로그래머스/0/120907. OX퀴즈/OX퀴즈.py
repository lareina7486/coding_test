def solution(quiz):
    arr=[]
    for i in quiz:
        s = i.split()
        if s[1]=='+':
            result=int(s[0])+int(s[2])
        else:
            result=int(s[0])-int(s[2])
        
        if result==int(s[4]):
            arr.append("O")
        else: arr.append("X")
    return arr
            