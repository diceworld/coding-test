from sys import stdin


def find(_parent, _x):  # 부모 찾기
    while _x != _parent[_x]:
        _x = _parent[_x]
    return _x


def union(_parent, _a, _b):  # 합치기
    _a = find(_parent, _a)
    _b = find(_parent, _b)

    if _a > _b:
        _parent[_a] = _b
    elif _b > _a:
        _parent[_b] = _a


N = int(stdin.readline())  # 행성의 수
parent = [0] * (N + 1)  # 부모 리스트
edges = []  # 간선 리스트
graph = []  # 그래프
result = 0  # cost 결과
count = 0  # union 횟수

for i in range(1, N + 1):  # 부모 초기화
    parent[i] = i

for _ in range(N):  # 그래프 입력
    graph.append(list(map(int, stdin.readline().split())))

for i in range(N):  # 그래프 > 간선 리스트
    for j in range(i + 1, N):
        edges.append((graph[i][j], i + 1, j + 1))

edges.sort()  # cost 기준 정렬

for cost, a, b in edges:  # MST 생성 및 cost 계산
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost
        count += 1

    if count == N + 1:
        break

print(result)  # cost 결과 출력
