from collections import deque
from sys import stdin

N, M, R = map(int, stdin.readline().split())  # 정점, 간선, 시작 정점
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):  # 간선 정보 입력
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):  # 간선 정렬
    graph[i].sort()


def bfs(_graph, _start, _visited):  # bfs
    q = deque()  # queue 선언
    q.append(_start)

    count = 1  # 시작 정점은 1로 입력
    _visited[_start] = count

    while q:  # queue 가 빌때 까지
        _v = q.popleft()

        for _i in graph[_v]:
            if _visited[_i]:
                continue

            count += 1
            _visited[_i] = count
            q.append(_i)


bfs(graph, R, visited)  # bfs 호출

for i in range(1, N + 1):
    print(visited[i])
