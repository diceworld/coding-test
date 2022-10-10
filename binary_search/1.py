"""
정수형태의 고유번호를 부여한 부품이 N개 있을 때 M개 종류의 부품이 다 존재하는지 확인하는 프로그램을 작성하시오.
(이진탐색)
"""
n = int(input())  # N
part_list = list(map(int, input().split()))  # 부품 리스트

m = int(input())  # M
desired_part_list = list(map(int, input().split()))  # 원하는 부품 리스트

part_list.sort()


def binary_search(array, target, start, end):
    if start >= end:
        return 'no'

    mid = (start + end) // 2

    if array[mid] == target:
        return 'yes'
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


for i in range(m):
    print(binary_search(part_list, desired_part_list[i], 0, n), end=' ')


