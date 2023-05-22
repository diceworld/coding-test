from sys import stdin

n = int(stdin.readline())  # 계단의 갯수
points = [0] * (n + 1)
d = [0] * (n + 1)  # dp 리스트

for i in range(1, n + 1):
    points[i] = int(stdin.readline())  # 게단의 점수

d[1] = points[1]

if n > 1:
    d[2] = points[1] + points[2]

if n > 2:
    d[3] = max(points[1] + points[3], points[2] + points[3])

for i in range(3, n + 1):
    d[i] = max(d[i - 3] + points[i - 1] + points[i], d[i - 2] + points[i])

print(d[n])
