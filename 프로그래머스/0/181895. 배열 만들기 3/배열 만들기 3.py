def solution(arr, intervals):
    list =[]
    for start,end in intervals:
        list+=arr[start:end+1]
    return list