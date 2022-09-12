"""
정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서
3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.
정수 N 은 0 보다 크거나 갖고 23보다 작거나 같다.
"""
n = int(input())  # N
count = 0  # 모든 경우의 수
second_count_in3 = 0  # 00 ~ 59 사이에 3이 포함된 경우의 수 확인
minute_count_in3 = 0  # 00:00 ~ 59:59 사이에 3이 포함된 경우의 수 확인

for i in range(60):
    if '3' in str(i):
        second_count_in3 += 1

for m in range(60):
    if '3' in str(m):
        minute_count_in3 += 60
    else:
        minute_count_in3 += second_count_in3

for h in range(n + 1):
    if '3' in str(h):
        count += 3600
    else:
        count += minute_count_in3

print(count)
