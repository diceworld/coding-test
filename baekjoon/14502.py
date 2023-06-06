from sys import stdin
from copy import deepcopy
from collections import deque

DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, m = map(int, stdin.readline().split())  # 세로 크기 n, 가로 크기 m
graph = []  # 0: 빈칸, 1: 벽, 2: 바이러스
wall_area = [False] * (n * m)  # 벽
virus_area = [False] * (n * m)  # 바이러스
added_wall = []  # 추가한 벽
max_area = 0  # 최대 안전 영역


def check(x, y):  # 갈수 있는 영역 인지 확인
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    return True


def dfs(x, y):
    virus = False
    area = 0
    q = deque()
    q.append((x, y))
    visited[y * m + x] = True

    while q:
        now_x, now_y = q.popleft()  # 현재 x, y
        area += 1

        if graph[now_y][now_x] == 2:
            virus = True

        for dx, dy in DIR:
            mx = now_x + dx
            my = now_y + dy

            if check(mx, my) and not visited[my * m + mx]:
                q.append((mx, my))
                visited[my * m + mx] = True

    if virus:  # 바이러스가 있는 공간이면
        area = 0

    return area


for _ in range(n):  # 맵 입력
    graph.append(list(map(int, stdin.readline().split())))

for y in range(n):
    for x in range(m):
        if graph[y][x] == 1:
            wall_area[y * m + x] = True
        elif graph[y][x] == 2:
            virus_area[y * m + x] = True

for i in range(n * m):
    if wall_area[i] or virus_area[i]:
        continue

    for j in range(i + 1, n * m):
        if wall_area[j] or virus_area[j]:
            continue

        for k in range(j + 1, n * m):
            if wall_area[k] or virus_area[k]:
                continue

            added_wall = [i, j, k]
            visited = deepcopy(wall_area)  # 방문 여부
            visited[i] = True
            visited[j] = True
            visited[k] = True
            area = 0

            for y in range(n):
                for x in range(m):
                    if not visited[y * m + x]:
                        area += dfs(x, y)

            if max_area < area:
                max_area = area

print(max_area)
