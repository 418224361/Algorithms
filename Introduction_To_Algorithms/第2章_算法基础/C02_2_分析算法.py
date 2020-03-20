def lx22_2(array):  # 选择排序
    for i in range(len(array) - 2):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


if __name__ == '__main__':
    A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(lx22_2(A))
