"""
정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서
3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.
정수 N 은 0 보다 크거나 갖고 23보다 작거나 같다.
"""
n = int(input())  # N
count = 0  # 모든 경우의 수

for h in range(n + 1):
    if '3' in str(h):
        count += 3600
        continue

    for m in range(60):
        if '3' in str(m):
            count += 60
            continue

        for s in range(60):
            if '3' in str(s):
                count += 1

print(count)
