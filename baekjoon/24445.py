from collections import deque
from sys import stdin


def bfs(s):
    q = deque()
    q.append(s)
    seq = 0
    visited[s] = True

    while q:
        v = q.popleft()  # 노드
        seq += 1
        sequence[v] = seq

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)


n, m, r = map(int, stdin.readline().split())  # 정점의 수, 간선의 수, 시작 정점
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
sequence = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, stdin.readline().split())  # 정점
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort(reverse=True)

bfs(r)

for i in range(1, n + 1):
    print(sequence[i])
