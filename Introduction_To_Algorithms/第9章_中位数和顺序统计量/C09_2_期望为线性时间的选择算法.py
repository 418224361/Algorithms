from Introduction_To_Algorithms.第7章_快速排序.第7章_第1节_快速排序的描述 import randomized_partition


# 在线性时间内找出数组中第i大的元素
def randomized_select(array, i, p=None, r=None):
    # 假设array的所有元素是互异的
    if p is None and r is None:
        p = 0
        r = len(array)
        if p == r:
            return None
        elif i < 0 or i > r - p:
            raise(ValueError('{}超出序列范围'.format(i)))
    array, index = randomized_partition(array, p, r)
    if p == r:
        return array
    if index + 1 == i:
        return array[index]
    elif index + 1 > i:
        return randomized_select(array, i, p, index)
    else:
        return randomized_select(array, i, index, r)


if __name__ == '__main__':
    c = [13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21, 34, 52, 56, 24, 78, 32]
    print(sorted(c[::]))
    print(randomized_select(c, 17))

    nul = []
    print(randomized_select(nul, 0))
