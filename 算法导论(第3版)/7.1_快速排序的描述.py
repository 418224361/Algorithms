def partition(array, p, r):
    """
    对数组array[p:r]进行分割，不含r
    :param array:
    :param p:
    :param r:
    :return:
    """
    if p > r:
        return ValueError
    else:
        x = array[r - 1]
        i = p - 1
        for j in range(p, r-1):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[r-1] = array[r - 1],array[i + 1]
    return array, i + 1


if __name__ == '__main__':
    A = [2, 8, 7, 1, 3, 5, 6, 4]
    print(partition(A, 0, len(A)))
