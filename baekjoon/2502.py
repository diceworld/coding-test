from sys import stdin

d, k = map(int, stdin.readline().split())  # 넘어온 날, 떡의 개수
dp = [0] * (d + 1)
dp[1] = 1
dp[2] = 1

for i in range(3, d + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

a_count = dp[d - 2]
b_count = dp[d - 1]
a = 0
b = 0

for _b in range(1, k + 1):
    _a = (k - (_b * b_count)) / a_count

    if (k - (_b * b_count)) % a_count == 0 and _a <= _b:
        a = int(_a)
        b = _b
        break

print(a)
print(b)
