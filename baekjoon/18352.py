from sys import stdin
import heapq


def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        dist, now = heapq.heappop(q)  # 코스트, 현재 노드

        if dist > distance[now]:
            continue

        for v, w in graph[now]:
            cost = dist + w

            if distance[v] > cost:
                distance[v] = cost
                heapq.heappush(q, (cost, v))


INF = int(1e9)  # 무한
n, m, k, x = map(int, stdin.readline().split())  # 도시, 도로, 거리정보, 출발도시의 번호
graph = [[] for _ in range(n + 1)]  # 그래프
distance = [INF] * (n + 1)  # 거리 정보
count = 0

for _ in range(m):
    u, v = map(int, stdin.readline().split())  # 2개의 도시
    w = 1  # 코스트
    graph[u].append([v, w])


dijkstra(x)  # 다익스트라 호출

for i in range(1, n + 1):
    if distance[i] == k:
        count += 1
        print(i)

if count == 0:  # k 의 거리에 해당하는 값이 없는 경우
    print(-1)
