from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10000)


def init(node, start, end):
    if start == end:
        tree[node] = numbers[start]
    else:
        mid = (start + end) // 2
        init(node * 2, start, mid)
        init(node * 2 + 1, mid + 1, end)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]


def query(node, start, end, left, right):
    if start > right or end < left:
        return 0

    if start >= left and end <= right:
        return tree[node]

    mid = (start + end) // 2
    left_sum = query(node * 2, start, mid, left, right)
    right_sum = query(node * 2 + 1, mid + 1, end, left, right)
    return left_sum + right_sum


n, m = map(int, stdin.readline().split())  # n: 수의 개수, m: 합을 구해야 하는 횟수
numbers = list(map(int, stdin.readline().split()))  # 수열
tree = [0] * (n * 4)  # 트리

init(1, 0, n - 1)

for _ in range(m):
    i, j = map(int, stdin.readline().split())  # i, j : 구간
    print(query(1, 0, n - 1, i - 1, j - 1))
