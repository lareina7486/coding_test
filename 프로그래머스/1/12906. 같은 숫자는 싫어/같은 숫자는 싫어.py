def solution(arr):
    stack = []

    for i in arr:
        if not stack or i != stack[-1]:
            stack.append(i)
    
    return stack