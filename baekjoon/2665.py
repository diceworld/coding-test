import heapq
from sys import stdin

INF = int(1e9)
n = int(stdin.readline())
maze = [['' for _ in range(n + 1)]]

graph = [[] for _ in range(n * n + 1)]
distance = [INF] * (n * n + 1)

for _ in range(n):
    maze.append([''] + list(stdin.readline().rstrip()))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        target = (i - 1) * n + j
        # 상
        if i > 1:
            if maze[i - 1][j] == "1":
                graph[target].append([target - n, 0])
            else:
                graph[target].append([target - n, 1])
        # 하
        if i < n:
            if maze[i + 1][j] == "1":
                graph[target].append([target + n, 0])
            else:
                graph[target].append([target + n, 1])
        # 좌
        if j > 1:
            if maze[i][j - 1] == "1":
                graph[target].append([target - 1, 0])
            else:
                graph[target].append([target - 1, 1])
        # 우
        if j < n:
            if maze[i][j + 1] == "1":
                graph[target].append([target + 1, 0])
            else:
                graph[target].append([target + 1, 1])


def dijkstra(_s):
    q = []
    distance[_s] = 0
    heapq.heappush(q, (0, _s))

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for g in graph[now]:
            cost = dist + g[1]

            if distance[g[0]] > cost:
                distance[g[0]] = cost
                heapq.heappush(q, (cost, g[0]))


dijkstra(_s=1)

print(distance[n * n])
