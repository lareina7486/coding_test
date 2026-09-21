def solution(myString):
    new_string=''
    for ch in myString:
        if ch<'l':
            new_string+='l'
        else:
            new_string+=ch
    return new_string