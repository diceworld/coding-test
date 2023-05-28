from sys import stdin

T = int(stdin.readline())  # 테스트 케이스

for _ in range(T):
    N = int(stdin.readline())  # N 번째 삼각형

    d = [0] * (N + 1)

    if N > 0:
        d[1] = 1
    if N > 1:
        d[2] = 1
    if N > 2:
        d[3] = 1

    for i in range(4, N + 1):
        d[i] = d[i - 2] + d[i - 3]

    print(d[N])
