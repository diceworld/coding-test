import sys
from sys import stdin

sys.setrecursionlimit(200000)

N, M, R = map(int, stdin.readline().split())  # 정점, 간선, 시작 정점
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
count = 1

for _ in range(M):  # 간선 입력
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):  # 간선 정렬
    graph[i].sort()


def dfs(_graph, _v, _visited):  # 그래프, 타겟 정점, 방문 기록
    global count
    visited[_v] = count

    for _i in _graph[_v]:
        if not visited[_i]:
            count += 1
            dfs(_graph, _i, _visited)


dfs(graph, R, visited)  # dfs 호출

for i in range(1, N + 1):  # 결과 출력
    print(visited[i])
