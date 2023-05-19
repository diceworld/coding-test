from sys import stdin


def find(_parent, _x):
    while _x != _parent[_x]:
        _x = _parent[_x]
    return _x


def union(_parent, _a, _b):
    _a = find(_parent, _a)
    _b = find(_parent, _b)

    if _a > _b:
        _parent[_a] = _b
    elif _b > _a:
        _parent[_b] = _a


T = int(stdin.readline())  # 테스트 케이스의 수

for _ in range(T):
    N, M = map(int, stdin.readline().split())  # 국가의 수, 비행기의 종류
    parent = [0] * (N + 1)  # 부모 리스트
    result = 0
    edges = []  # 간선 리스트

    for i in range(1, N + 1):  # 부모 리스트 초기화
        parent[i] = i

    for _ in range(M):
        a, b = map(int, stdin.readline().split())  # 도시 a, b
        edges.append((a, b))

    for a, b in edges:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            result += 1

    print(result)
