import sys
from sys import stdin

sys.setrecursionlimit(100000)

N = int(stdin.readline())  # 도시의 수
M = int(stdin.readline())  # 여행할 도시의 수
parent = [0] * (N + 1)  # 부모 리스트 초기화


def find(_parent, _v):
    if _parent[_v] != _v:
        _parent[_v] = find(_parent, _parent[_v])
    return _parent[_v]


def union(_parent, _a, _b):
    _a = find(_parent, _a)
    _b = find(_parent, _b)

    if _a < _b:
        _parent[_b] = _a
    else:
        _parent[_a] = _b


for i in range(1, N + 1):
    parent[i] = i

for i in range(N):
    path_list = list(map(int, stdin.readline().split()))

    for j in range(N):
        if path_list[j] == 1:
            union(parent, i + 1, j + 1)

plan_list = list(map(int, stdin.readline().split()))

for i in range(M):
    plan_list[i] = find(parent, plan_list[i])

if len(set(plan_list)) == 1:
    print("YES")
else:
    print("NO")
