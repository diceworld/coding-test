"""
N x M 으로 이루어진 직사각형의 맵에서 캐릭터가 움직일 때 캐릭터가 방문한 칸의 수를 출력하는 프로그램을 만드시오.
맵의 칸은 육지와 바다로 되어 있으며, 캐릭터는 육지로만 이동할 수 있습니다.
맵의 각 칸은 (A, B) 로 나타낼 수 있고, A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수이다.
캐릭터는 상하좌우로 움직일 수 있고, 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 갈 곳을 정합니다.
캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽방향으로 회전한 다음 왼쪽으로 한 칸을 전진합니다.
왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽방향으로 회전만 수행합니다.
만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸의 경우에는, 바라보는 방향을 유지한 채로 한칸 뒤로 갑니다.
단, 이떄 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춥니다.
캐릭터가 있는 칸의 좌표 a, b 와 바라보는 방향 d가 주어졌을 때 캐릭터가 방문한 칸의 수를 출력하시오.
- 방향 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽
- 맵타일 0: 육지, 1: 바다, 2: 육지(가본 곳)
"""
n, m = map(int, input().split())  # N, M
a, b, d = map(int, input().split())  # A, B, d
map_dict = []  # 맵
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북, 동, 남, 서
count = 1  # 방문한 칸의 수
check = 0  # 체크한 횟수

# 맵 입력
for i in range(n):
    map_dict.append(list(map(int, input().split())))

# 현재 위치를 가본 곳으로 설정
map_dict[a][b] = 2

while True:
    # 이동 가능 영역 체크 값 설정
    check += 1

    # 왼쪽 방향으로 회전
    if d == 0:
        d = 3
    else:
        d -= 1

    # 다음 행선지 좌표 계산
    next_a = a + direction[d][0]
    next_b = b + direction[d][1]
    
    # 다음 행선지 확인
    if map_dict[next_a][next_b] == 0:
        a = next_a
        b = next_b
        count += 1
        check = 0
        map_dict[a][b] = 2
        continue

    if check != 4:
        continue

    next_a = a + direction[(d + 2) % 4][0]
    next_b = b + direction[(d + 2) % 4][1]

    if map_dict[next_a][next_b] == 1:
        break

    a = next_a
    b = next_b
    check = 0

print(count)
