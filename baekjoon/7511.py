from sys import stdin


def find(x):
    while parent[x] != parent[parent[x]]:
        parent[x] = parent[parent[x]]
    return parent[x]


def union(u, v):
    u = find(u)
    v = find(v)

    if u > v:
        parent[u] = v
    elif v > u:
        parent[v] = u


t = int(stdin.readline())  # 테스트 케이스의 수

for i in range(1, t + 1):
    n = int(stdin.readline())  # 유저의 수
    k = int(stdin.readline())  # 친구 관계의 수
    parent = list(range(n + 1))  # 부모 리스트

    for _ in range(k):
        u, v = map(int, stdin.readline().split())  # 친구 관계
        union(u, v)

    m = int(stdin.readline())  # 구할 관계의 수

    print(f"Scenario {i}:")

    for _ in range(m):
        u, v = map(int, stdin.readline().split())  # 구해야 하는 쌍
        if find(u) == find(v):
            print("1")
        else:
            print("0")

    print("")
