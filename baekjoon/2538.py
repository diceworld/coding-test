from sys import stdin
from collections import deque

m, n, k = map(int, stdin.readline().split())  # 세로, 가로, 직사각형의 수

graph = [[0] * n for _ in range(m)]  # 모눈종이
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 방향


def paint(x1, y1, x2, y2):  # 직사각형 좌표를 받아 1로 채우기
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[j][i] = 1


def check(x, y):  # 접근할 수 없는 위치인지 확인
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    return True


for _ in range(k):  # 직사각형 입력 받기
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    paint(x1, y1, x2, y2)


def bfs(x, y):
    if graph[y][x] != 0:  # 해당영역이 1이 아니면 접근할 수 없는 곳
        return 0

    q = deque()
    q.append((x, y))
    graph[y][x] = 1
    visit_count = 0  # 방문한 칸

    while q:
        cx, cy = q.popleft()  # 현재 위치
        visit_count += 1

        for dx, dy in d:  # 상하좌우 방향별 체크
            if check(cx + dx, cy + dy) and graph[cy + dy][cx + dx] == 0:  # 접근할 수 있다면
                q.append((cx + dx, cy + dy))
                graph[cy + dy][cx + dx] = 1  # 방문 처리

    return visit_count  # 최종 방문한 칸 리턴


count = 0  # 영역 수
widths = []  # 영역 넓이

for i in range(m):
    for j in range(n):
        result = bfs(j, i)  # 모든 칸에 대해 bfs 실행

        if result != 0:
            count += 1
            widths.append(result)

print(count)
widths.sort()

for width in widths:
    print(width, end=" ")
