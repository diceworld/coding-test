"""
여행가 A 는 N X N 크기의 정사각형 공간위에 서있고, 가장 왼쪽 위 좌표는 (1, 1) 이며,
가장 오른쪽 좌표는 (N, N) 에 해당한다. 여행가 A 는 상, 하, 좌, 우 방향으로 이동할 수 있으며,
시작 좌표는 항상 (1, 1) 이다.
여행가 A 가 이동할 계획서에 L, R, U, D 로 이동할 방향이 나타내어지고, 여행가는 이에 따라 이동한다.
단, 여행가 A 가 정사각형 공간을 벗어나는 움직임은 무시된다.
"""
n = int(input())  # N
direction_list = list(map(str, input().split()))  # 여행 계획서
position = (1, 1)  # 위치

direction_map = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0),
}

for direction in direction_list:
    next_position = (position[0] + direction_map[str(direction)][0], position[1] + direction_map[str(direction)][1])

    if next_position[0] < 1 or next_position[0] > n or next_position[1] < 1 or next_position[1] > n:
        continue

    position = next_position

print(position[0], position[1])
