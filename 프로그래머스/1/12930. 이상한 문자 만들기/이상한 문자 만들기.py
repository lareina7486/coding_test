def solution(s):
    word=[]
    word=s.split(' ')
    str=''
    for temp in word:
        for i, ch in enumerate(temp):
            if i%2==0:
                str+=temp[i].upper()
            else:
                str+=temp[i].lower()
        str+=' '
    return str[:-1]