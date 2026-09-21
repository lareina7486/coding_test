def solution(arr):
    stack = []
    top = -1
    for i in arr:
        if not stack or i!=stack[top]:
            stack.append(i)
            top+=1
    return stack