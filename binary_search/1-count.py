"""
정수형태의 고유번호를 부여한 부품이 N개 있을 때 M개 종류의 부품이 다 존재하는지 확인하는 프로그램을 작성하시오.
(계수정렬)
"""
n = int(input())  # N
part_list = list(map(int, input().split()))  # 부품 리스트

m = int(input())  # M
desired_part_list = list(map(int, input().split()))  # 원하는 부품 리스트

have_list = [0] * 1000001

for i in part_list:
    have_list[i] = 1

for i in desired_part_list:
    result = 'yes' if have_list[i] == 1 else 'no'
    print(result, end=' ')
