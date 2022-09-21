array = [6, 9, 5, 1, 3, 0, 8, 2, 4, 7]

for i in range(len(array)):
    min_idx = i  # 가장 작은 원소의 인덱스

    for j in range(i + 1, len(array)):
        if array[min_idx] > array[j]:
            min_idx = j

    array[i], array[min_idx] = array[min_idx], array[i]

print(array)
