from sys import stdin

n = int(stdin.readline().rstrip())

for _ in range(n):
    result = str(stdin.readline().rstrip())

    total_point = 0
    point = 0

    for x in result:
        if x == "O":
            point += 1
            total_point += point
        else:
            point = 0

    print(total_point)
