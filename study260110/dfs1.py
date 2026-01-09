
# DFS - 한 방향으로 끝까지 탐색 후 되돌아와서 다른 경로 검색
# 재귀, 스택으로 구현

graph = {
    1: [2, 3],
    2: [4],
    3: [],
    4: []
}

visited = set()

def dfs(node):
    if node in visited:
        return

    visited.add(node)
    print(node)

    for next_node in graph[node]:
        dfs(next_node)

dfs(1)      # 1 2 4 3