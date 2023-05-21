from sys import stdin

n = int(stdin.readline())  # 수열 A 의 크기 N
s = list(map(int, stdin.readline().split()))  # 수열 A
d = [1] * n  # dp 리스트

# 전체 수열 반복
for i in range(1, n):
    # 현재 수열 보다 이전 수열에 대해 반복
    for j in range(i):
        # 수열 값이 더 큰 경우 확인
        if s[j] > s[i]:
            d[i] = max(d[i], d[j] + 1)

print(max(d))
