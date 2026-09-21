def solution(myStr):
    l=[]
    l=myStr.replace('a',' ').replace('b',' ').replace('c',' ').strip().split()
    if not l: return ["EMPTY"]
    else: return myStr.strip().split()