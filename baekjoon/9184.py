from sys import stdin

d = []  # 메모이제이션 리스트

for i in range(101):
    d.append([])
    for j in range(101):
        d[i].append([0] * 101)


def w(_a, _b, _c):
    _x = _a + 50  # - 값을 위한 처리
    _y = _b + 50
    _z = _c + 50

    if d[_x][_y][_z] != 0:
        return d[_x][_y][_z]
    if _a <= 0 or _b <= 0 or _c <= 0:
        return 1
    if _a > 20 or _b > 20 or _c > 20:
        d[_x][_y][_z] = w(20, 20, 20)
        return d[_x][_y][_z]
    if _a < _b < _c:
        d[_x][_y][_z] = w(_a, _b, _c - 1) + w(_a, _b - 1, _c - 1) - w(_a, _b - 1, _c)
        return d[_x][_y][_z]

    d[_x][_y][_z] = w(_a - 1, _b, _c) + w(_a - 1, _b - 1, _c) + w(_a - 1, _b, _c - 1) - w(_a - 1, _b - 1, _c - 1)
    return d[_x][_y][_z]


while True:
    a, b, c = map(int, stdin.readline().split())

    if a == b == c == -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")
