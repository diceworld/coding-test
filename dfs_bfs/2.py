"""
여러 마리의 괴물이 있는 N x M 크기의 미로에서 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오.
시작지점은 (1, 1)이고 미로의 출구는 (N, M) 이며, 한번에 한 칸씩 움직일 수 있다.
괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있고, 칸을 셀 떄는 시작 칸과 마지막 칸을 모두 포함한다.
"""
from collections import deque

n, m = map(int, input().split())  # N, M
maze = []  # 미로

for _ in range(n):
    maze.append(list(map(int, input())))

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 좌, 우, 상, 하


# 미로를 순서대로 방문하면서 카운트 추가
def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + direction[i][0]
            ny = y + direction[i][1]

            # 영역 밖인 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 벽인 경우
            if maze[nx][ny] == 0:
                continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    return maze[n - 1][m - 1]


print(bfs(0, 0))
