from sys import setrecursionlimit
from sys import stdin

setrecursionlimit(10000)
INF = int(1e9)


def init(node, start, end):
    if start == end:
        tree[node] = numbers[start]
    else:
        mid = (start + end) // 2
        init(node * 2, start, mid)
        init(node * 2 + 1, mid + 1, end)
        tree[node] = min(tree[node * 2], tree[node * 2 + 1])


def query(node, start, end, left, right):
    if start > right or end < left:
        return INF

    if start >= left and end <= right:
        return tree[node]

    mid = (start + end) // 2
    left_min = query(node * 2, start, mid, left, right)
    right_min = query(node * 2 + 1, mid + 1, end, left, right)
    return min(left_min, right_min)


def update(node, start, end, index, value):
    if index < start or index > end:
        return

    if start == end:
        tree[node] = value
    else:
        mid = (start + end) // 2
        update(node * 2, start, mid, index, value)
        update(node * 2 + 1, mid + 1, end, index, value)
        tree[node] = min(tree[node * 2], tree[node * 2 + 1])


n = int(stdin.readline())  # 수열의 크기
tree = [0] * (n * 4)  # 트리
numbers = list(map(int, stdin.readline().split()))  # 수열
init(1, 0, n - 1)


m = int(stdin.readline())  # 쿼리의 갯수

for _ in range(m):
    t, i, j = map(int, stdin.readline().split())

    if t == 1:  # update
        update(1, 0, n - 1, i - 1, j)
    elif t == 2:  # 최소값 구하기
        print(query(1, 0, n - 1, i - 1, j - 1))
