def solution(cipher, code):
    ans=''
    for i in range(1, len(cipher)//code+1):
        ans += cipher[code*i-1]
    return ans