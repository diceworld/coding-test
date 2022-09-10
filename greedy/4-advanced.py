"""
어떠한 수 N이 1이 될때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
단 두번째 연산은 N이 K로 나누어떨어질때만 선택할 수 있다.
1. N에서 1을 뺀다
2. N을 K로 나눈다.
N과 K 가 주어질 때 N이 1이 될 때까지 최소횟수를 구하시오.
"""
n, k = map(int, input().split())  # N, K
count = 0  # 실행 횟수

# 반복문을 통해 1이 될 때까지 실행
while True:
    if n == 1:
        break
    elif n % k == 0:
        count += 1
        n /= k
    else:
        count += n % k
        n -= n % k


print(count)
