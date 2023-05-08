import heapq
from sys import stdin

INF = int(1e9)
v, e = map(int, stdin.readline().split())
s = int(stdin.readline())

graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)

for _ in range(e):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((b, c))


def dijkstra(_s):
    q = []
    heapq.heappush(q, (0, _s))
    distance[_s] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(_s=s)

for i in range(1, v + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
