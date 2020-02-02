import math


def merge(array, p, q, r):
    # 对序列array[p:r+1]在下标q处拆分成两个序列后进行归并排序
    if p > q + 1 or q > r:
        raise ValueError('merge函数的分割点不在区间范围内')
    elif not isinstance(array, list):
        return [array]
    left_array = array[p:q + 1]
    right_array = array[q + 1:r+1]
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
    if i < left_len:
        new_array.extend(left_array[i::])
    elif j < right_len:
        new_array.extend(right_array[j::])
    array[p:r+1] = new_array
    # print(new_array)
    return array


def merge_sort(array, p, r):
    """
    对序列array[p, r]进行排序
    :param array: array的子列是待排序序列
    :param p: 待排序子列在array的起始位置下标值，array的第一个元素p=0
    :param r: 待排序子列在array的终止位置下标值，array的最后一个元素r=len(array)-1
    :return: 完成排序的子列
    """
    if p == r:
        return array[p]
    elif p < r:
        q = math.floor((p + r) / 2)
        left_array = merge_sort(array, p, q)
        right_array = merge_sort(array, q+1, r)
        if p == q:
            array[p] = left_array
        elif q+1 == r:
            array[q+1] = right_array
        else:
            array[p:q+1] = left_array[p:q+1]
            array[q+1:r+1] = right_array[q+1:r+1]
        return merge(array, p, q, r)


if __name__ == '__main__':
    a = [5, 3, 1, 9, 7, 2, 4, 6, 8, 10]
    print(merge_sort(a, 0, 9))
