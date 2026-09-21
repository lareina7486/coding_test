def solution(my_string):
    sum=0
    arr = my_string.split()
    sum+=int(arr[0])
    for i in range(1,len(arr),2):
        if arr[i]=='+': sum+=int(arr[i+1])
        else: sum-=int(arr[i+1])
    return sum