"""
8 x 8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오.
이 때 행위치를 표현할때는 1부터 8로. 열 위치를 표현할 때는 a부터 h로 표현한다.
"""
val = input()  # 입력값
row = ord(val[0].lower()) - 96  # 행
col = int(val[1])

count = 0  # 모든 경우의 수

movable_list = [
    (-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, -1), (2, 1), (1, -2), (1, 2)
]

for movable in movable_list:
    result = (movable[0] + row, movable[1] + col)

    if result[0] <= 0 or result[0] > 8 or result[1] <= 0 or result[1] > 8:
        continue

    count += 1

print(count)
