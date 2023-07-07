from sys import stdin


def find(x):  # 부모 찾기
    while parent[x] != parent[parent[x]]:
        parent[x] = parent[parent[x]]
    return parent[x]


def union(u, v):  # 합치기
    u = find(u)
    v = find(v)

    if u > v:
        parent[u] = v
    elif v > u:
        parent[v] = u


while True:
    m, n = map(int, stdin.readline().split())  # 집의 수, 길의 수
    graph = []  # 그래프
    parent = list(range(n + 1))  # 부모
    cost = 0  # 결과

    if m == 0 and n == 0:  # 0, 0 이 입력된 경우 종료
        break

    for _ in range(n):
        x, y, z = map(int, stdin.readline().split())  # 집1, 집2, 거리
        graph.append((z, x, y))

    graph.sort()

    for z, x, y in graph:
        if find(x) != find(y):  # 연결 가능 (절약 불가능 구간)
            union(x, y)
        else:  # 연결 불가능 (절약 가능 구간)
            cost += z

    print(cost)  # 절약한 비용
