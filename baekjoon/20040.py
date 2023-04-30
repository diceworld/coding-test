import sys
from sys import stdin

sys.setrecursionlimit(1000000)

n, m = map(int, stdin.readline().split())  # 점의 개수, 진행된 차례의 수
parent = [0] * n
cycle_start_no = 0

for i in range(n):
    parent[i] = i


def find(_parent, _v):
    if _parent[_v] != _v:  # 루트 노드가 아닌 경우
        _parent[_v] = find(_parent, _parent[_v])
    return _parent[_v]


def union(_parent, _a, _b):
    _a = find(_parent, _a)
    _b = find(_parent, _b)

    if _a > _b:
        _parent[_a] = _b
    else:
        _parent[_b] = _a


def check_cycle(_parent, _a, _b):
    _a = find(_parent, _a)
    _b = find(_parent, _b)

    if _a == _b:
        return True
    return False


for i in range(1, m + 1):
    a, b = map(int, stdin.readline().split())

    if check_cycle(parent, a, b):
        cycle_start_no = i
        break

    union(parent, a, b)

print(cycle_start_no)
