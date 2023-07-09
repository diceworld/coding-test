from sys import stdin
import heapq


def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for v, w in graph[now]:
            cost = dist + w

            if distance[v] > cost:
                distance[v] = cost
                heapq.heappush(q, (cost, v))


INF = int(1e9)  # 무한
n = int(stdin.readline())  # 도시의 개수
m = int(stdin.readline())  # 버스의 개수
graph = [[] for _ in range(n + 1)]  # 버스 비용
distance = [INF] * (n + 1)  # 거리

for _ in range(m):
    u, v, w = map(int, stdin.readline().split())  # 출발도시, 도착도시, 코스트
    graph[u].append((v, w))

s, e = map(int, stdin.readline().split())  # 출발도시, 도착도시

dijkstra(s)
print(distance[e])
