from sys import stdin

n = int(stdin.readline().rstrip())

remain = 0

for _ in range(n):
    student, apple = map(int, stdin.readline().rstrip().split())

    remain += apple % student

print(remain)
