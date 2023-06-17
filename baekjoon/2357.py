from sys import setrecursionlimit
from sys import stdin

setrecursionlimit(10000)
INF = int(1e10)


def init(node, start, end):
    if start == end:
        min_tree[node] = numbers[start]
        max_tree[node] = numbers[start]
    else:
        mid = (start + end) // 2
        init(node * 2, start, mid)
        init(node * 2 + 1, mid + 1, end)
        min_tree[node] = min(min_tree[node * 2], min_tree[node * 2 + 1])
        max_tree[node] = max(max_tree[node * 2], max_tree[node * 2 + 1])


def query(node, start, end, left, right):
    if start > right or end < left:
        return INF, -1

    if start >= left and end <= right:
        return min_tree[node], max_tree[node]

    mid = (start + end) // 2
    left_min, left_max = query(node * 2, start, mid, left, right)
    right_min, right_max = query(node * 2 + 1, mid + 1, end, left, right)
    return min(left_min, right_min), max(left_max, right_max)


n, m = map(int, stdin.readline().split())  # 수의 갯수, 최소 최대 값 확인 수
numbers = []  # 수 리스트
min_tree = [0] * (n * 4)  # 최소 트리
max_tree = [0] * (n * 4)  # 최대 트리

for _ in range(n):  # 수 리스트 입력
    numbers.append(int(stdin.readline()))

init(1, 0, n - 1)

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    min_val, max_val = query(1, 0, n - 1, a - 1, b - 1)
    print(str(min_val) + " " + str(max_val))
