"""
메모제이션을 활용한 피보나치 수열
"""
d = [0] * 100


def fibonacci(x):
    """
    피보나치 함수 (탑다운 다이나믹 프로그래밍 방식)
    """
    if x in [1, 2]:
        return 1

    # 이미 계산한 적이 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]

    # 아직 계산한 적이 없는 문제라면 피보나치 결과 반환
    d[x] = fibonacci(x - 1) + fibonacci(x - 2)
    return d[x]


print(fibonacci(99))
