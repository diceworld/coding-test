from collections import deque
from sys import stdin

# . 빈필드, # 울타리, o 양, v 늑대
r, c = map(int, stdin.readline().split())  # 열, 행
graph = []  # 마당
visited = [False] * (r * c)  # 방문 여부 리스트
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 방향
total_o = 0  # 전체 양의 수
total_v = 0  # 전체 늑대의 수

for _ in range(r):  # 마당 리스트 입력
    graph.append(list(str(stdin.readline().rstrip())))

for y in range(r):  # 울타리 방문 처리
    for x in range(c):
        if graph[y][x] == "#":
            visited[y * c + x] = True


def check(x, y):  # 갈 수 있는 곳인지 확인
    if x < 0 or x >= c or y < 0 or y >= r:
        return False
    return True


def dfs(x, y):
    if visited[y * c + x]:
        return 0, 0  # 양의 수, 늑대의 수

    q = deque()
    q.append((x, y))
    visited[y * c + x] = True
    o = 0
    v = 0

    while q:
        x1, y1 = q.popleft()

        if graph[y1][x1] == "o":  # 양인 경우
            o += 1
        elif graph[y1][x1] == "v":  # 늑대인 경우
            v += 1

        for x2, y2 in dir:  # 상 하 좌 우 확인
            if check(x1 + x2, y1 + y2) and not visited[(y1 + y2) * c + x1 + x2]:
                visited[(y1 + y2) * c + x1 + x2] = True
                q.append((x1 + x2, y1 + y2))

    if o > v:  # 양이 더 많은 경우
        v = 0
    elif v > 0:  # 늑대가 더 많거나 같고 늑대가 0 이상인 경우
        o = 0

    return o, v  # 양의 수, 늑대의 수


for y in range(r):  # 울타리 방문 처리
    for x in range(c):
        o, v = dfs(x, y)
        total_o += o
        total_v += v

print(total_o, total_v)  # 출력
