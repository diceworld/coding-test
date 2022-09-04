"""
다양한 수로 이루어진 배열이 있을 떄 주어진 수들을 M번 더하여 가장 큰수를 만드는 법칙이다.
단 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.
서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주한다.
배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 큰 수의 법칙에 따른 결과를 출력하시오.
"""
n, m, k = map(int, input().split())  # N, M, K
arr = list(map(int, input().split()))  # 배열
count = int(m / (k + 1)) * k  # 배열에서 가장 큰수 + 2번째로 큰수 셋트의 횟수

arr.sort()  # 배열 정렬
first = arr[-1]  # 배열에서 가장 큰 수
second = arr[-2]  # 배열에서 2번째로 큰 수

result = count * first  # 셋트결과 저장
result += (m - count) * second  # 나머지는 큰수로 저장

print(result)
