from sys import stdin

N = int(stdin.readline())
d = [0] * (N + 1)

d[1] = 1

if N > 1:
    d[2] = 2

for i in range(3, N + 1):
    d[i] = (d[i - 1] + d[i - 2]) % 15746

print(d[N])
