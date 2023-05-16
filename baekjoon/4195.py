from sys import stdin, setrecursionlimit

setrecursionlimit(1000000)


T = int(stdin.readline())  # 테스트 케이스의 수


def find(_parent, _v):
    if _parent[_v] != _v:
        _parent[_v] = find(_parent, _parent[_v])

    return _parent[_v]


def union(_parent, _count, _a, _b):
    _a = find(_parent, _a)
    _b = find(_parent, _b)

    if _a < _b:
        _parent[_b] = _a
    elif _b < _a:
        _parent[_a] = _b
    else:
        return

    c = _count[_a] + _count[_b]
    _count[_a] = c
    _count[_b] = c


for _ in range(T):
    F = int(stdin.readline())  # 친구 관계의 수
    parent = {}  # 부모 dict
    count = {}  # 카운트 dict

    for _ in range(F):
        a, b = map(str, stdin.readline().rstrip().split())  # 친구 a, 친구 b

        if a not in parent:
            parent[a] = a
            count[a] = 1
        if b not in parent:
            parent[b] = b
            count[b] = 1

        union(parent, count, a, b)

        print(count[find(parent, a)])
