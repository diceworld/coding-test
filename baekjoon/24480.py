import sys
from sys import stdin

sys.setrecursionlimit(200000)  # 재귀 함수 호출 수 추가

N, M, R = map(int, stdin.readline().split())  # 정점, 간선, 시작 정점
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
count = 1

for _ in range(M):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    graph[i].sort(reverse=True)


def dfs(_graph, _v, _visited):
    global count
    visited[_v] = count

    for _i in _graph[_v]:
        if not visited[_i]:
            count += 1
            dfs(_graph, _i, _visited)


dfs(graph, R, visited)

for i in range(1, N + 1):
    print(visited[i])
