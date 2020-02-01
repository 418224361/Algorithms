def merge(array, p, q, r):
    # 对序列array的从下标p到下标q部分子列在下标r处拆分后归并排序
    if p > q + 1 or q + 1 > r:
        raise ValueError('merge函数的分割点不在区间范围内')
    left_array = array[p:q + 1]
    right_array = array[q + 1:r]
    left_len = len(left_array)
    right_len = len(right_array)
    new_array = []
    i = j = 0
    while i <= left_len - 1 and j <= right_len - 1:
        if left_array[i] <= right_array[j]:
            new_array.append(left_array[i])
            i += 1
        else:
            new_array.append(right_array[j])
            j += 1
    if i <= left_len:
        new_array.extend(left_array[i::])
    elif j <= right_array:
        new_array.extend(right_array[j::])
    return new_array


if __name__ == '__main__':
    a = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    print(merge(a, 0, 4, 9))
