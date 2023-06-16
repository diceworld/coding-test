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


def update(node, start, end, index, diff):
    if index < start or index > end:
        return

    tree[node] += diff

    if start != end:
        mid = (start + end) // 2
        update(node * 2, start, mid, index, diff)
        update(node * 2 + 1, mid + 1, end, index, diff)


n, m, k = map(int, stdin.readline().split())  # 수의 갯수, 수의 변경이 일어나는 횟수, 구간의 합을 구하는 횟수
numbers = []  # 수열
tree = [0] * (n * 4)  # 트리

for _ in range(n):  # 수열 입력
    numbers.append(int(stdin.readline()))

init(1, 0, n - 1)

for _ in range(m + k):
    a, b, c = map(int, stdin.readline().split())

    if a == 1:  # 업데이트 하기
        diff = c - numbers[b - 1]
        numbers[b - 1] = c
        update(1, 0, n - 1, b - 1, diff)
    elif a == 2:  # 구간합 구하기
        print(query(1, 0, n - 1, b - 1, c - 1))
