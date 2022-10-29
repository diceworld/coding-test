"""
shortest path 1
"""

INF = int(1e9)

# 노드의 개수 및 간선의 개수 이력
n, m = map(int, input().split())

# 2차원 리스트 생성
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신 비용 0
for a in range(1, n + 1):
    graph[a][a] = 0

# 각 간선에 대한 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 최종 목적지 노드 X 와 거쳐갈 노드 K 입력
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과로 거리 측정
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우, -1을 출력
if distance >= INF:
    print("-1")
else:
    print(distance)
