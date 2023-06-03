from sys import stdin

hour, minute = map(int, stdin.readline().rstrip().split())
cooking_time = int(stdin.readline().rstrip())

cooking_hour = cooking_time // 60
cooking_minute = cooking_time % 60

hour += cooking_hour
minute += cooking_minute

if minute >= 60:
    hour += 1
    minute -= 60

if hour >= 24:
    hour -= 24

print("{} {}".format(hour, minute))
