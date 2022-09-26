"""
수열을 내림차순으로 정렬하는 프로그램을 만드시오.
첫째줄에 수열에 속해 있는 수의 개수 N이 주어진다 (1 <= N <= 500)
둘째줄부터 N + 1 번째 줄까지 N개의 수가 입력된다.
"""
n = int(input())  # N
sequence = []  # 수열

for i in range(n):
    sequence.append(int(input()))

sequence.sort(reverse=True)

for i in sequence:
    print(i, end=' ')
