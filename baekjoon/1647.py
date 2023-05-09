from sys import stdin


def find(_parent, _x):  # 찾기
    while _x != _parent[_x]:
        _x = _parent[_x]
    return _x


def union(_parent, _a, _b):  # 합치기
    _a = find(_parent, _a)
    _b = find(_parent, _b)

    if _a > _b:
        _parent[_a] = _b
    elif _b > _a:
        _parent[_b] = _a


N, M = map(int, stdin.readline().split())  # 집의 갯수, 길의 갯수
parent = [0] * (N + 1)  # 부모 리스트
edges = []  # 간선 리스트
result = 0  # MST cost 결과
max_cost = 0  # 가장 높은 cost

for i in range(1, N + 1):
    parent[i] = i

for _ in range(M):
    A, B, C = map(int, stdin.readline().split())  # A번 집, B번 집, 유지비
    edges.append((C, A, B))

edges.sort()

for cost, a, b in edges:
    if find(parent, a) != find(parent, b):  # circle 이 안되는 경우
        union(parent, a, b)
        result += cost

        if cost > max_cost:
            max_cost = cost

print(result - max_cost)  # 가장 높은 cost 의 길을 없애서 마을을 2개로 분리
