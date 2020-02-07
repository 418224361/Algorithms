import math


def merge(array, p, q, r):
    # 对序列array[p:r+1]在下标q处拆分成两个序列后进行归并排序
    if p > q + 1 or q > r:
        raise ValueError('merge函数的分割点不在区间范围内')
    elif not isinstance(array, list):
        return [array]
    left_array = array[p:q + 1]
    right_array = array[q + 1:r + 1]
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
    array[p:r + 1] = new_array
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
        right_array = merge_sort(array, q + 1, r)
        if p == q:
            array[p] = left_array
        elif q + 1 == r:
            array[q + 1] = right_array
        else:
            array[p:q + 1] = left_array[p:q + 1]
            array[q + 1:r + 1] = right_array[q + 1:r + 1]
        return merge(array, p, q, r)


# 2.3-4 用递归实现插入排序
def lx23_4(array):
    if len(array) == 1:
        return array
    else:
        key = array[-1]
        new_array = lx23_4(array[:-1])
        j = len(new_array) - 1
        while j >= 0 and new_array[j] > key:
            j -= 1
        new_array.insert(j + 1, key)
        return new_array


# 2.3-5 定义二分法查找函数
def bi_search(ordered_array, p, r, v):
    if p + 1 == r and v == ordered_array[p]:
        return p
    elif p + 1 == r and v != ordered_array[p]:
        return False
    pointer = math.floor((p + r) / 2)
    if ordered_array[pointer] == v:
        return pointer
    elif ordered_array[pointer] < v:
        return bi_search(ordered_array, pointer, r + 1, v)
    else:
        return bi_search(ordered_array, p, pointer, v)


# 2.3-6 用二分查找优化插入排序
def bi_search_opt(ordered_array, p, r, v):
    # 对递增(非递减)序列orderd_array[p, r]进行二分查找，返回值为小于等于v的最右侧数据的下标
    if p + 1 == r:
        return p
    pointer = math.floor((p + r) / 2)
    if ordered_array[pointer] == v:
        return pointer
    # 向下取整时，需要对序列最右侧处理
    elif ordered_array[pointer] < v and pointer < len(ordered_array) - 2:
        return bi_search_opt(ordered_array, pointer, r, v)
    elif ordered_array[pointer] < v and pointer == len(ordered_array) - 2:
        return len(ordered_array) - 1
    else:
        return bi_search_opt(ordered_array, p, pointer, v)


def insertion_sort_opt(array):
    # 使用二分法优化后的插入排序
    if len(array) == 1:
        return array
    else:
        key = array[-1]
        new_array = lx23_4(array[:-1])
        j = len(new_array) - 1
        idx = bi_search_opt(new_array, 0, len(new_array) - 1, key)
        new_array.insert(idx + 1, key)
        return new_array


# 2.3-7
def lx23_7(array, v):
    # array的元素为整数。找出array中的两个元素，使其和为v
    ordered_array = merge_sort(array, 0, len(array)-1)
    i = 0
    j = len(ordered_array) - 1
    while i <= j:
        sumary = ordered_array[i] + ordered_array[j]
        if sumary == v:
            return ordered_array[i], ordered_array[j]
        elif sumary < v:
            i += 1
        elif sumary > v:
            j -= 1
    return False


# 思考题2.1
def merge_sort_opt(array, p, r, k):
    """
    对序列array[p, r]进行归并排序，当序列长度小于k时，使用插入排序
    :param array: array的子列是待排序序列
    :param p: 待排序子列在array的起始位置下标值，array的第一个元素p = 0
    :param r: 待排序子列在array的终止位置下标值，array的最后一个元素r = len(array) - 1
    :param k: 当序列长度小于等于k时，使用插入排序
    :return: 完成排序的子列
    """
    if r - p < k:
        return insertion_sort_opt(array[p, r])
    elif p < r:
        q = math.floor((p + r) / 2)
        left_array = merge_sort(array, p, q)
        right_array = merge_sort(array, q + 1, r)
        if p == q:
            array[p] = left_array
        elif q + 1 == r:
            array[q + 1] = right_array
        else:
            array[p:q + 1] = left_array[p:q + 1]
            array[q + 1:r + 1] = right_array[q + 1:r + 1]
        return merge(array, p, q, r)


# 思考题2.1
def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(i, len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


if __name__ == '__main__':
    A = [3, 41, 52, 26, 38, 57, 9, 49]
    B = [3, 9, 26, 38, 41, 49, 52, 57]
    print(merge_sort(A, 0, len(A) - 1))
    print(lx23_4(A))
    print(bi_search_opt(B, 0, 7, 3))
    print(bi_search_opt(B, 0, 7, 37))
    print(bi_search_opt(B, 0, 7, 39))
    print(bi_search_opt(B, 0, 7, 57))
    print(bi_search_opt(B, 0, 7, 58))
    print(insertion_sort_opt(A))
    print(lx23_7(A, 50))
    print(merge_sort_opt(A, 0, 7, 3))
