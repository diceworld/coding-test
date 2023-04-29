import heapq
from sys import stdin

INF = int(1e9)

N, E = map(int, stdin.readline().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

V1, V2 = map(int, stdin.readline().split())


def dijkstra(_s, distance):
    q = []
    distance[_s] = 0
    heapq.heappush(q, (0, _s))

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance


def get_shortest_distance(_s, _e):
    distance = [INF] * (N + 1)  # 초기화
    distance = dijkstra(_s=_s, distance=distance)
    return distance[_e]


result_1_to_v1 = get_shortest_distance(_s=1, _e=V1)
result_v1_to_v2 = get_shortest_distance(_s=V1, _e=V2)
result_v2_to_n = get_shortest_distance(_s=V2, _e=N)

result_1_to_v2 = get_shortest_distance(_s=1, _e=V2)
result_v2_to_v1 = get_shortest_distance(_s=V2, _e=V1)
result_v1_to_n = get_shortest_distance(_s=V1, _e=N)

if result_1_to_v1 == INF or result_v1_to_v2 == INF or result_v2_to_n == INF:
    result_v1 = -1
else:
    result_v1 = result_1_to_v1 + result_v1_to_v2 + result_v2_to_n

if result_1_to_v2 == INF or result_v2_to_v1 == INF or result_v1_to_n == INF:
    result_v2 = -1
else:
    result_v2 = result_1_to_v2 + result_v2_to_v1 + result_v1_to_n

if result_v1 == -1 and result_v2 == -2:
    print(-1)
elif result_v1 == -1:
    print(result_v2)
elif result_v2 == -1:
    print(result_v1)
else:
    print(min(result_v1, result_v2))
