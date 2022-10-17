"""
길이 M 만큼의 떡을 구하기 위해 각각 다른 크기의 줄지어진 떡을
높이 H인 절단기로 절단하여 구한다고 한다. 이 때 가장 H 값의 최대크기를 구하시오.

첫째 줄에 떡의 갯수 N 과 요청한 길이 M이 주어진다.
둘째 줄에는 떡의 개별 높이가 주어진다.
"""
n, m = map(int, input().split())  # N, M

rice_cakes = list(map(int, input().split()))  # 떡의 개별 높이

start = 0
end = max(rice_cakes)

h = 0  # H


while start <= end:
    total = 0
    mid = (start + end) // 2

    for x in rice_cakes:
        if x > mid:
            total += x - mid

    if total < m:
        end = mid - 1
    else:
        h = mid
        start = mid + 1

print(h)
