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
        tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % 1000000007


def query(node, start, end, left, right):
    if start > right or end < left:
        return 1

    if start >= left and end <= right:
        return tree[node]

    mid = (start + end) // 2
    left_mul = query(node * 2, start, mid, left, right)
    right_mul = query(node * 2 + 1, mid + 1, end, left, right)
    return left_mul * right_mul


def update(node, start, end, index, value):
    if index < start or index > end:
        return

    if start == end:
        tree[node] = value
    else:
        mid = (start + end) // 2
        update(node * 2, start, mid, index, value)
        update(node * 2 + 1, mid + 1, end, index, value)
        tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % 1000000007


n, m, k = map(int, stdin.readline().split())  # 수의 개수, 변경 횟수, 곱 횟수
numbers = []  # 수 리스트
tree = [0] * (n * 4)  # 트리

for _ in range(n):  # 수 입력
    numbers.append(int(stdin.readline()))

init(1, 0, n - 1)

for _ in range(m + k):
    a, b, c = map(int, stdin.readline().split())

    if a == 1:
        numbers[b - 1] = c
        update(1, 0, n - 1, b - 1, c)
    elif a == 2:
        print(int(query(1, 0, n - 1, b - 1, c - 1) % 1000000007))
