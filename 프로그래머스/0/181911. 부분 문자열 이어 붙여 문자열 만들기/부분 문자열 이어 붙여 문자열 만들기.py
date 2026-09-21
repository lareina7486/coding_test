def solution(my_strings, parts):
    str=''
    for s, (start,end) in zip(my_strings, parts):
            str+=s[start:end+1]
    return str