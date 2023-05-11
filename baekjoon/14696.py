from sys import stdin

n = int(stdin.readline().rstrip())


def calc_point(symbols):
    points = [0, 0, 0, 0, 0]

    for symbol in symbols:
        points[symbol] += 1

    return points


for _ in range(n):
    a_in = map(int, stdin.readline().rstrip().split())
    b_in = map(int, stdin.readline().rstrip().split())
    _, a = next(a_in), list(a_in)
    _, b = next(b_in), list(b_in)
    a_points = calc_point(a)
    b_points = calc_point(b)

    for i in range(4, 0, -1):
        if a_points[i] > b_points[i]:
            print("A")
            break
        elif a_points[i] < b_points[i]:
            print("B")
            break
        elif i == 1:
            print("D")
