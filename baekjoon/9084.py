from sys import stdin

t = int(stdin.readline().rstrip())


def solve(_coins, _m):
    dp = [0] * 10001

    for _coin in _coins:
        dp[_coin] += 1
        for i in range(_coin + 1, _m + 1):
            dp[i] += dp[i - _coin]

    return dp[_m]


for _ in range(t):
    n = int(stdin.readline().rstrip())
    coins = list(map(int, stdin.readline().rstrip().split()))
    m = int(stdin.readline().rstrip())

    print(solve(_coins=coins, _m=m))
