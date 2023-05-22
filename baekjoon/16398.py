import heapq
from sys import stdin


def find(_parent, x):  # 집합 찾기
    while x != _parent[x]:
        _parent[x] = _parent[_parent[x]]  # 경로 압축
        x = _parent[x]
    return x


def union(u, v):  # 집합 합치기
    u = find(parent, u)
    v = find(parent, v)

    if u > v:
        parent[u] = v
    elif u < v:
        parent[v] = u


n = int(stdin.readline())  # 행성의 수
parent = list(range(n + 1))  # 부모 테이블
q = []
matrix = []  # 행성간의 플로우 관리 비용
result = 0  # MST 구성 비용

for _ in range(n):  # 인접 행렬 입력
    matrix.append(list(map(int, stdin.readline().split())))

for i in range(1, n):  # 인접 행렬을 인접 리스트로 변경
    for j in range(i):
        heapq.heappush(q, (matrix[i][j], i + 1, j + 1))

while q:
    w, u, v = heapq.heappop(q)  # cost, 정점 u, 정점 v
    if find(parent, u) != find(parent, v):
        union(u, v)
        result += w

print(result)
