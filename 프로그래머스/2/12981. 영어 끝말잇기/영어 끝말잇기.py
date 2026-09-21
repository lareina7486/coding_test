def solution(n, words):
    list=[]
    
    for i, w in enumerate(words):
        if i==0:
            list.append(w)
            continue
        else:
            if words[i-1][-1]!=words[i][0]:
                return [i%n+1, i//n+1]
            if len(w)==1:
                return [i%n+1, i//n+1]
            if w in list:
                return [i%n+1, i//n+1]
            
            list.append(w)    
            
    else:
        return [0,0]