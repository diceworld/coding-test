"""
N개의 자연수로 구성된 두 개의 배열 A 와 B가 있다.
A와 B에 있는 원소 하나를 골라서 서로 바꾸는 바꿔치기 연산을 최대 K번 수행할 수 있을 때,
배열 A의 모든 원소의 합이 최댓값이 되도록 프로그램을 작성하시오.
"""
n, k = map(int, input().split())  # N, K
a_list = list(map(int, input().split()))  # A 배열
b_list = list(map(int, input().split()))  # B 배열

# b의 가장 큰 수를 a의 가장 작은 수로 변경
for _ in range(k):
    a_list.sort()
    b_list.sort()

    if a_list[0] < b_list[-1]:
        a_list[0], b_list[-1] = b_list[-1], a_list[0]
    else:
        break

print(sum(a_list))
