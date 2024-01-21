from collections import deque

def bfs(matrix, start, target_color, visited):
    H, W = len(matrix), len(matrix[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    queue = deque([start])
    visited[start[0]][start[1]] = True
    score = 1

    while queue:
        current = queue.popleft()

        for dx, dy in directions:
            nx, ny = current[0] + dx, current[1] + dy

            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and matrix[nx][ny] == target_color:
                visited[nx][ny] = True
                queue.append((nx, ny))
                score += 1

    return score

def max_score(matrix):
    H, W = len(matrix), len(matrix[0])
    max_score = 0
    visited = [[False] * W for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if not visited[i][j]:
                target_color = matrix[i][j]
                score = bfs(matrix, (i, j), target_color, visited)
                max_score = max(max_score, score)

    return max_score

# 入力例
H, W = 4, 4
matrix = [
    [1, 2, 3, 1],
    [2, 2, 3, 1],
    [1, 2, 3, 1],
    [3, 3, 2, 2]
]

result = max_score(matrix)
print(result)
