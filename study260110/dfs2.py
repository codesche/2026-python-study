
# DFS 실습 - 2차원 배열 탐색 (격자 DFS 맛보기)
grid = [
    [1, 1, 0],
    [0, 1, 0],
    [1, 0, 1]
]

rows = len(grid)
cols = len(grid[0])
visited = [[False] * cols for _ in range(rows)]

def dfs(x, y):
    if x < 0 or y < 0 or x >= rows or y >= cols:
        return
    if visited[x][y] or grid[x][y] == 0:
        return

    visited[x][y] = True

    dfs(x + 1, y)
    dfs(x - 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)

dfs(0, 0)