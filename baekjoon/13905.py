from sys import stdin
from collections import deque


def find(x):
    while parent[x] != parent[parent[x]]:
        parent[x] = parent[parent[x]]
    return parent[x]


def union(u, v):
    u = find(u)
    v = find(v)

    if u > v:
        parent[u] = v
    elif v > u:
        parent[v] = u


def bfs(s):
    q = deque()
    q.append((s, int(1e9)))
    visited[s] = True
    result = int(1e9)

    while q:
        now, cost = q.popleft()

        if now == e:
            result = cost
            break

        for v, w in tree[now]:
            if not visited[v]:
                visited[v] = True
                cost = min(cost, w)
                q.append((v, cost))

    return result


n, m = map(int, stdin.readline().split())  # 집의 개수, 다리의 수
s, e = map(int, stdin.readline().split())  # 숭이의 출발 위치, 혜빈이의 위치
graph = []  # 다리의 정보
parent = list(range(n + 1))  # 부모 정보
tree = [[] for _ in range(n + 1)]  # 트리
visited = [False] * (n + 1)  # 방문 여부

for _ in range(m):
    u, v, w = map(int, stdin.readline().split())  # 집과 다리의 무게 제한
    graph.append((w, u, v))

graph.sort(reverse=True)

for w, u, v in graph:
    if find(u) != find(v):
        union(u, v)
        tree[u].append((v, w))
        tree[v].append((u, w))

result = bfs(s)

if result == int(1e9):
    print("0")
else:
    print(result)
