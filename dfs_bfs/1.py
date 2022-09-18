"""
N x M 크기의 얼음틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.
"""
n, m = map(int, input().split())  # N, M
count = 0  # 아이스크림의 개수
ice_tray = []  # 얼음틀

for i in range(n):
    ice_tray.append(list(map(int, input())))


# 인접한 모든 트레이를 방문처리 (칸막이가 존재하는 부분처럼 1로 변경)
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if ice_tray[x][y] == 0:
        ice_tray[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True

    return False


# 모든 얼음틀 확인
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            count += 1

print(count)
