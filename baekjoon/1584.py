from sys import stdin
import heapq


def check(x, y):
    if 0 <= x <= MAX and 0 <= y <= MAX and graph[y][x] != -1:
        return True
    return False


def dijkstra(x, y):
    q = []
    visited[y * (MAX + 1) + x] = True
    heapq.heappush(q, (0, x, y))
    distance[y * (MAX + 1) + x] = 0

    while q:
        cost, cx, cy = heapq.heappop(q)

        if distance[cy * (MAX + 1) + cx] > cost:
            distance[cy * (MAX + 1) + cx] = cost

        for dx, dy in d:
            mx = cx + dx
            my = cy + dy

            if check(mx, my) and not visited[my * (MAX + 1) + mx] and graph[my][mx] + cost <= distance[my * (MAX + 1) + mx]:
                visited[my * (MAX + 1) + mx] = True
                heapq.heappush(q, (graph[my][mx] + cost, mx, my))


def set_area(x1, y1, x2, y2, type):
    min_x = min(x1, x2)
    max_x = max(x1, x2)
    min_y = min(y1, y2)
    max_y = max(y1, y2)
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            graph[y][x] = type


MAX = 500  # 최대치
INF = int(1e9)  # 무한
graph = [[0 for _ in range(MAX + 1)] for _ in range(MAX + 1)]  # 구역 정보 0: 안전한 구역, 1: 위험한 구역, -1: 죽음의 구역
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 방향
distance = [INF] * ((MAX + 1) * (MAX + 1))  # 거리 정보
visited = [False] * ((MAX + 1) * (MAX + 1))  # 방문 정보

n = int(stdin.readline())  # 위험한 구역의 수

for _ in range(n):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    set_area(x1, y1, x2, y2, 1)

m = int(stdin.readline())  # 죽음의 구역의 수

for _ in range(m):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    set_area(x1, y1, x2, y2, -1)

dijkstra(0, 0)

if distance[(MAX + 1) * (MAX + 1) - 1] == INF:
    print("-1")
else:
    print(distance[(MAX + 1) * (MAX + 1) - 1])
