"""
숫자카드 게임은 여러개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한장을 뽑는 게임이다.
1. 숫자가 쓰인 카드들이 N x M 형태로 놓여 있다. 이 떄 N은 행의 개수를 의미하며, M은 열의 개수를 의미한다.
2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
3. 그 다음 선택된 행에 포함된 카드들 중 가장숫자가 낮은 카드를 뽑아야 한다.
4. 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여
최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.
"""
n, m = map(int, input().split())  # N, M
card_list = []  # 배열

# 전체 행을 입력받아 배열 구성
for i in range(n):
    card_list.append(sorted(list(map(int, input().split()))))

card_list.sort(reverse=True)  # 배열 정렬

result = card_list[0][0]  # 뽑은 카드의 수

print(result)
