from sys import stdin

n, k = map(int, stdin.readline().rstrip().split())
points = []


for _ in range(n):
    in_val = map(int, stdin.readline().rstrip().split())
    no, medals = next(in_val), tuple(in_val)
    points.append({"no": no, "gold": medals[0], "silver": medals[1], "bronze": medals[2], "rank": 1})

points.sort(key=lambda x: (x["gold"], x["silver"], x["bronze"]), reverse=True)

rank = 0
k_gold = 0
k_silver = 0
k_bronze = 0

for i in range(n):
    if points[i]["no"] == k:
        rank = i + 1
        k_gold = points[i]["gold"]
        k_silver = points[i]["silver"]
        k_bronze = points[i]["bronze"]
        break

for i in range(rank - 2, 0, -1):
    if k_gold != points[i]["gold"]:
        break
    if k_silver != points[i]["silver"]:
        break
    if k_bronze != points[i]["bronze"]:
        break
    rank -= 1

print(rank)
