def solution(myString):
    return ''.join(['A' if s=='a' else s for s in myString.lower()])