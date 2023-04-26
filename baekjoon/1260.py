from collections import deque
from sys import stdin

n, m, v = map(int, stdin.readline().rstrip().split())

graph = [[] for _ in range(n + 1)]
dfs_result = []
bfs_result = []

for _ in range(m):
    start, end = map(int, stdin.readline().rstrip().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(1, n + 1):
    graph[i].sort()


def dfs(_graph, _v, _visited):
    dfs_result.append(_v)
    _visited[_v] = 1

    for _point in _graph[_v]:
        if _visited[_point] == 0:
            dfs(_graph, _point, _visited)


visited = [0] * (n + 1)
dfs(graph, v, visited)

for result in dfs_result:
    print(result, end=" ")
print()


def bfs(_graph, _start, _visited):
    queue = deque([_start])
    visited[_start] = 1

    while queue:
        _v = queue.popleft()
        bfs_result.append(_v)

        for _point in graph[_v]:
            if _visited[_point] == 0:
                queue.append(_point)
                _visited[_point] = 1


visited = [0] * (n + 1)
bfs(graph, v, visited)

for result in bfs_result:
    print(result, end=" ")
