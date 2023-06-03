from sys import stdin
from collections import deque


DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n = int(stdin.readline())  # 그리드의 크기
graph = []  # 그리드
rgb_visited = [False] * (n * n)
rb_visited = [False] * (n * n)
rgb_count = 0
rb_count = 0


for _ in range(n):
    graph.append(list(str(stdin.readline().rstrip())))  # 그리드 입력


def check(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return True


def rgb_dfs(x, y):
    q = deque()
    rgb_visited[y * n + x] = True
    color = graph[y][x]
    q.append((x, y))

    while q:
        nx, ny = q.popleft()  # 현재 x, y

        for dx, dy in DIR:  # 4방향
            mx = nx + dx  # 이동할 x
            my = ny + dy  # 이동할 y

            if check(mx, my) and not rgb_visited[my * n + mx] and graph[my][mx] == color:
                q.append((mx, my))
                rgb_visited[my * n + mx] = True


def rb_dfs(x, y):
    q = deque()
    rb_visited[y * n + x] = True
    color = graph[y][x]
    q.append((x, y))

    while q:
        nx, ny = q.popleft()  # 현재 x, y

        for dx, dy in DIR:  # 4방향
            mx = nx + dx  # 이동할 x
            my = ny + dy  # 이동할 y

            if check(mx, my) and not rb_visited[my * n + mx]:
                if color in ["R", "G"] and graph[my][mx] in ["R", "G"]:
                    q.append((mx, my))
                    rb_visited[my * n + mx] = True
                elif graph[my][mx] == color:
                    q.append((mx, my))
                    rb_visited[my * n + mx] = True


for y in range(n):
    for x in range(n):
        if not rgb_visited[y * n + x]:
            rgb_dfs(x, y)
            rgb_count += 1

for y in range(n):
    for x in range(n):
        if not rb_visited[y * n + x]:
            rb_dfs(x, y)
            rb_count += 1

print(rgb_count, end=" ")
print(rb_count)
