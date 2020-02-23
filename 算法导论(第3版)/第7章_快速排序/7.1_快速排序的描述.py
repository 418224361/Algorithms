def partition(array, p, r):
    """
    对数组array[p:r]进行分割，不含r
    :return: 返回分割后的数组以及主元(pivot element)
    """
    if p > r:
        return ValueError
    else:
        x = array[r - 1]
        i = p - 1
        for j in range(p, r - 1):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[r - 1] = array[r - 1], array[i + 1]
    return array, i + 1


def quick_sort(array):
    if len(array) == 1:
        return array[0]
    else:
        array, q = partition(array, 0, len(array))
        left_array = quick_sort(array[0:q])
        right_array = quick_sort(array[q:len(array)])
        array = left_array.extend(right_array)
        return array


if __name__ == '__main__':
    A = [2, 8, 7, 1, 3, 5, 6, 4]
    # print(partition(A, 0, len(A)))
    quick_sort(A)
