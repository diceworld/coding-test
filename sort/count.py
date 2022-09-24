array = [0, 6, 1, 2, 9, 5, 8, 0, 5, 9, 7, 3, 1, 4, 2, 1]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i * count[i], end=' ')
