from sys import setrecursionlimit
from sys import stdin

setrecursionlimit(10000)
INF = int(1e6)


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


def update(node, start, end, index, value):
    if index < start or index > end:
        return

    if start == end:
        min_tree[node] = value
        max_tree[node] = value
    else:
        mid = (start + end) // 2
        update(node * 2, start, mid, index, value)
        update(node * 2 + 1, mid + 1, end, index, value)
        min_tree[node] = min(min_tree[node * 2], min_tree[node * 2 + 1])
        max_tree[node] = max(max_tree[node * 2], max_tree[node * 2 + 1])


t = int(stdin.readline())  # 테스트 케이스의 수

for _ in range(t):
    n, k = map(int, stdin.readline().split())  # dvd 의 수, 사건의 수
    numbers = list(range(n))
    min_tree = [0] * (n * 4)
    max_tree = [0] * (n * 4)

    init(1, 0, n - 1)

    for _ in range(k):
        q, a, b = map(int, stdin.readline().split())

        if q == 0:  # dvd 변경
            a_val = numbers[a]
            b_val = numbers[b]
            numbers[a], numbers[b] = b_val, a_val

            update(1, 0, n - 1, a, b_val)
            update(1, 0, n - 1, b, a_val)
        elif q == 1:  # dvd 대여
            min_val, max_val = query(1, 0, n - 1, a, b)

            if a == min_val and b == max_val:
                print("YES")
            else:
                print("NO")
