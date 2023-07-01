from sys import stdin


def find(x):  # 부모 찾기
    while parent[x] != parent[parent[x]]:
        parent[x] = parent[parent[x]]
    return parent[x]


def union(u, v):  # 합치기
    u = find(u)
    v = find(v)

    if u > v:
        parent[u] = v
    elif v > u:
        parent[v] = u


n = int(stdin.readline())  # 컴퓨터의 수
m = int(stdin.readline())  # 연결할 수 있는 선의 수
graph = []  # 그래프
parent = list(range(n + 1))  # 부모 정보
result = 0  # 결과

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())  # 컴퓨터1, 컴퓨터2, 코스트
    if a != b:
        graph.append((c, a, b))

graph.sort()

for c, a, b in graph:
    if find(a) != find(b):
        union(a, b)
        result += c

print(result)  # 결과 출력
