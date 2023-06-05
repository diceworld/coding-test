from sys import stdin

n = int(stdin.readline())  # 직사각형의 넓이
d = [0] * (n + 1)  # dp 리스트

d[1] = 1

if n > 1:
    d[2] = 2

for i in range(3, n + 1):
    # i - 2 에서 가로 2 막대를 채우는 횟수 + i - 1 에서 세로 2 막대를 채우는 횟수
    d[i] = d[i - 2] + d[i - 1]

print(d[n] % 10007)
