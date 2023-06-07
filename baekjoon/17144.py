from sys import stdin


def check(x, y):
    if x < 0 or x >= c or y < 0 or y >= r:
        return False
    if x == 0 and y in air_cleaner:
        return False
    return True


def diffusion():
    dust = [[0] * c for _ in range(r)]  # 미세 먼지 정보

    # 확산 미세 먼지 계산
    for y in range(r):
        for x in range(c):
            if area[y][x] not in (0, -1):
                area_dust = area[y][x]
                diffusion_dust = area_dust // 5

                for dx, dy in DIR:
                    mx = x + dx
                    my = y + dy

                    if check(mx, my):
                        dust[my][mx] += diffusion_dust
                        area_dust -= diffusion_dust

                area[y][x] = area_dust

    # 공기 청정기 영역 확인 (공기 청정기 영역으로 확산된 미세 먼지 제거)
    for y in air_cleaner:
        dust[y][0] = 0

    # 확산 미세 먼지를 영역에 적용
    for y in range(r):
        for x in range(c):
            area[y][x] += dust[y][x]


def operate():
    # 윗쪽 공기 청정기 가동
    for y in range(air_cleaner[0] - 2, -1, -1):
        area[y + 1][0] = area[y][0]
        area[y][0] = 0

    for x in range(1, c):
        area[0][x - 1] = area[0][x]
        area[0][x] = 0

    for y in range(1, air_cleaner[0] + 1):
        area[y - 1][c - 1] = area[y][c - 1]
        area[y][c - 1] = 0

    for x in range(c - 2, 0, -1):
        area[air_cleaner[0]][x + 1] = area[air_cleaner[0]][x]
        area[air_cleaner[0]][x] = 0

    # 아랫쪽 공기 청정기 가동
    for y in range(air_cleaner[1] + 2, r):
        area[y - 1][0] = area[y][0]
        area[y][0] = 0

    for x in range(1, c):
        area[r - 1][x - 1] = area[r - 1][x]
        area[r - 1][x] = 0

    for y in range(r - 2, air_cleaner[1] - 1, -1):
        area[y + 1][c - 1] = area[y][c - 1]
        area[y][c - 1] = 0

    for x in range(c - 2, 0, -1):
        area[air_cleaner[1]][x + 1] = area[air_cleaner[1]][x]
        area[air_cleaner[1]][x] = 0


DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 방향
r, c, t = map(int, stdin.readline().split())  # r: row 수, c: column 수, t: 초
area = []  # 방
air_cleaner = []  # 공기 청정기 y 좌표
dust_quantity = 0  # 미세 먼지 양

for _ in range(r):
    area.append(list(map(int, stdin.readline().split())))  # 방 정보 (-1: 공기 청정기)

for y in range(r):  # 공기 청정기 y 좌표 기록
    if area[y][0] == -1:
        air_cleaner.append(y)

for _ in range(t):  # t 초간 미세 먼지 확산 및 공기 청정기 가동
    # 미세 먼지 확산
    diffusion()

    # 공기 청정기 가동
    operate()

for y in range(r):
    for x in range(c):
        if area[y][x] not in (0, -1):
            dust_quantity += area[y][x]

print(dust_quantity)
