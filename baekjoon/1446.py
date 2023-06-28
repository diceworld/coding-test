from sys import stdin
import heapq


def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        dist, now = heapq.heappop(q)  # 거리, 현재 정점

        if dist > distance[now]:
            continue

        for v, w in graph[now]:
            cost = dist + w

            if distance[v] > cost:
                distance[v] = cost
                heapq.heappush(q, (cost, v))


INF = int(1e9)  # 무한
n, d = map(int, stdin.readline().split())  # 지름길의 개수, 고속도로의 길이
graph = [[] for _ in range(d + 1)]  # 그래프
distance = [INF] * (d + 1)  # 거리
points = [0]  # 포인트
result = 0  # 운전할 거리

for _ in range(n):
    u, v, w = map(int, stdin.readline().split())  # 시작, 종료, 코스트

    if u >= 0 and v <= d and v - u > w:
        graph[u].append([v, w])
        points.append(u)
        points.append(v)

points = list(set(points))
points.sort()

for i in range(len(points)):
    if i == len(points) - 1:
        u, v, w = points[i], d, d - points[i]
    else:
        u, v, w = points[i], points[i + 1], points[i + 1] - points[i]

    graph[u].append([v, w])

dijkstra(0)
print(distance[d])
