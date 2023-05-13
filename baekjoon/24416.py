from sys import stdin

n = int(stdin.readline())  # 피보나치 수를 구하고자 하는 값
d1 = [0] * (n + 1)  # 메모이제이션 리스트
d2 = [0] * (n + 1)  # 메모이제이션 리스트


def fib1(x):  # 탑다운 DP
    if x == 1 or x == 2:
        return 1

    if d1[x] != 0:
        return d1[x]

    d1[x] = fib1(x - 1) + fib1(x - 2)
    return d1[x]


def fib2(x):  # 보텀업 DP
    c = 0

    d2[1] = 1
    d2[2] = 1

    for i in range(3, x + 1):
        c += 1
        d2[i] = d2[i - 1] + d2[i - 2]

    return c


print(fib1(n), end=" ")
print(fib2(n))
