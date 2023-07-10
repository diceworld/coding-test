from sys import stdin
from collections import deque


def check(x, y):
    if 0 <= x < m and 0 <= y < n:
        return True
    return False


def dfs(x, y):
    q = deque()
    q.append((x, y))
    visited[y * m + x] = True
    shape = graph[y][x]

    while q:
        cx, cy = q.popleft()

        if shape == "-":
            my = cy
            mx = cx + 1
        else:  # "|"
            my = cy + 1
            mx = cx

        if check(mx, my) and not visited[my * m + mx] and graph[my][mx] == shape:
            visited[my * m + mx] = True
            q.append((mx, my))


n, m = map(int, stdin.readline().split())  # 세로 크기, 가로 크기
graph = []  # 바닥 장식
visited = [False] * (n * m)  # 방문 여부
result = 0  # 결과

for _ in range(n):
    graph.append(list(stdin.readline().rstrip()))  # 바닥 장식

for y in range(n):
    for x in range(m):
        if not visited[y * m + x]:
            result += 1
            dfs(x, y)

print(result)
