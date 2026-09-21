def solution(n):
    answer = [[0]*n for _ in range(n)]
    
    dx = [0, 1, 0, -1]  # 오른쪽, 아래, 왼쪽, 위
    dy = [1, 0, -1, 0]
    
    x = y = mode = 0
    for i in range(1, n*n + 1):
        answer[x][y] = i
        nx = x + dx[mode]
        ny = y + dy[mode]
        
        # 범위를 벗어나거나 이미 채운 경우 방향 전환
        if nx < 0 or nx >= n or ny < 0 or ny >= n or answer[nx][ny] != 0:
            mode = (mode + 1) % 4
            nx = x + dx[mode]
            ny = y + dy[mode]
        
        x, y = nx, ny
    
    return answer