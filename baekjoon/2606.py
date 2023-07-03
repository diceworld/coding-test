from sys import stdin
from collections import deque


def dfs(s):
    q = deque()
    q.append(s)
    visited[s] = True
    cnt = -1

    while q:
        v = q.popleft()  # 노드
        cnt += 1

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

    return cnt


n = int(stdin.readline())  # 컴퓨터의 수
m = int(stdin.readline())  # 연결 쌍
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, stdin.readline().split())  # 간선 정보
    graph[u].append(v)
    graph[v].append(u)


print(dfs(1))  # 1번 컴퓨터에 의해 바이러스에 걸리는 컴퓨터의 수
