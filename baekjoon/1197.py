from sys import stdin

v, e = map(int, stdin.readline().split())  # 정점의 개수, 간선의 개수
parent = list(range(v + 1))  # 부모 정보
graph = []  # 간선 정보
result = 0  # 트리 구성 비용

for _ in range(e):
    a, b, c = map(int, stdin.readline().split())  # 정점 a, 정점 b, 가중치 c
    graph.append((c, a, b))

graph.sort()  # 정점 정렬


def find(x):  # 조상 찾기
    while x != parent[x]:
        x = parent[x]
    return x


def union(a, b):  # 트리 합치기
    a = find(a)
    b = find(b)

    if a > b:
        parent[a] = b
    elif a < b:
        parent[b] = a


for c, a, b in graph:
    if find(a) != find(b):  # 사이클 확인
        union(a, b)
        result += c

print(result) # 최소 가중치 출력
