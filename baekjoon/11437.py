from collections import deque
from sys import stdin


def bfs(s):
    q = deque()
    q.append((0, s))
    depth[s] = 0

    while q:
        d, v = q.popleft()  # depth, 노드

        for i in graph[v]:
            if depth[i] == -1:
                depth[i] = d + 1
                parent[i] = v
                q.append((d + 1, i))


def lca(u, v):
    if depth[u] < depth[v]:  # 두 변수 값 치환
        u, v = v, u

    diff = depth[u] - depth[v]

    for _ in range(diff):
        u = parent[u]

    while u != v:
        u = parent[u]
        v = parent[v]
    return u


n = int(stdin.readline())  # 정점의 수
graph = [[] for _ in range(n + 1)]  # 그래프
depth = [-1] * (n + 1)
parent = [0] * (n + 1)

for _ in range(n - 1):  # 간선 정보
    u, v = map(int, stdin.readline().split())  # 2 정점
    graph[u].append(v)
    graph[v].append(u)

bfs(1)

m = int(stdin.readline())  # 공통 조상을 알고 싶은 쌍의 개수

for _ in range(m):
    u, v = map(int, stdin.readline().split())  # 쌍
    print(lca(u, v))
