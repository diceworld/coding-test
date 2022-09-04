"""
다양한 수로 이루어진 배열이 있을 떄 주어진 수들을 M번 더하여 가장 큰수를 만드는 법칙이다.
단 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.
서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주한다.
배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 큰 수의 법칙에 따른 결과를 출력하시오.
"""
n, m, k = map(int, input().split())  # N, M, K
arr = list(map(int, input().split()))  # 배열
result = 0  # 큰 수의 법칙으로 계산된 결과

arr.sort()  # 배열 정렬
first = arr[-1]  # 배열에서 가장 큰 수
second = arr[-2]  # 배열에서 2번째로 큰 수

for i in range(1, m + 1):
    if i % k == 0:
        result += second
    else:
        result += first

print(result)
