def solution(s):
    s=s.lower()
    words=s.split(' ')
    
    for i, word in enumerate(words):
        if word.strip() and word[0].isalpha():
            words[i] = word[0].upper()+word[1:]
    
    return ' '.join(words)