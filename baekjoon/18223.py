from collections import deque
from sys import stdin

INF = int(1e9)
v, e, p = map(int, stdin.readline().split())  # 정점, 간선, 건우의 위치 정점
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, stdin.readline().split())  # a > b 의 cost c
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(s):
    q = deque()
    q.append((0, s))
    distance[s] = 0

    while q:
        dist, now = q.popleft()  # 거리, 현재 정점

        if dist > distance[now]:
            continue

        for b, c in graph[now]:
            cost = dist + c

            if distance[b] > cost:
                distance[b] = cost
                q.append((cost, b))


distance = [INF] * (v + 1)
dijkstra(1)
d = distance[v]
d1 = distance[p]

distance = [INF] * (v + 1)
dijkstra(p)
d2 = distance[v]

if d == d1 + d2:
    print("SAVE HIM")
else:
    print("GOOD BYE")
