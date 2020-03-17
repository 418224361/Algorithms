import random


# 思考题8-4
def jug_partition(red, blue, p, r):
    # 首先从蓝桶中随机选出一个blue_pivot，用其对红桶做partition，同时找出相同的红桶red_pivot，再用red_pivot对蓝桶做partition.
    blue_pivot_index = random.randrange(p, r)
    blue_pivot = blue[blue_pivot_index]

    # 对红桶进行partition
    l = p - 1
    for j in range(p, r - 1):
        if red[j] < blue_pivot:
            l += 1
            red[l], red[j] = red[j], red[l]
        # 当red的第j个元素等于blue_pivot时，放到red最后
        elif red[j] == blue_pivot and j != r - 1:
            red_pivot = red.pop(j)
            red.insert(r - 1, red_pivot)
            # 下标j+1的元素，下标变为j，需要和pivot做一次比较，否则本次迭代会遗漏该元素
            if red[j] < blue_pivot:
                l += 1
                red[l], red[j] = red[j], red[l]
    red[l + 1], red[r - 1] = red[r - 1], red[l + 1]

    # 对蓝桶进行partition
    red_pivot = red[l + 1]
    m = p - 1
    for k in range(p, r - 1):
        if blue[k] < red_pivot:
            m += 1
            blue[m], blue[k] = blue[k], blue[m]
        # 当blue的第m个元素等于blue_pivot时，放到blue最后
        elif blue[k] == red_pivot and k != r - 1:
            blue_pivot = blue.pop(k)
            blue.insert(r - 1, blue_pivot)
            # 下标j+1的元素，下标变为j，需要和pivot做一次比较，否则本次迭代会遗漏该元素
            if blue[k] < blue_pivot:
                m += 1
                blue[m], blue[k] = blue[k], blue[m]
    blue[m + 1], blue[r - 1] = blue[r - 1], blue[m + 1]
    return red, blue, l + 1, m + 1


def jug_quick_sort(red, blue, p=None, r=None):
    if len(red) != len(blue):
        raise ValueError('长度不同')
    if p is None and r is None:
        p = 0
        r = len(red)
    if p >= r - 1:
        return red, blue
    else:
        red, blue, pivot_index, _ = jug_partition(red, blue, p, r)
        jug_quick_sort(red, blue, p, pivot_index)
        jug_quick_sort(red, blue, pivot_index, r)
        return red, blue


# 思考题8-5, 平均排序
def k_sort(array, k):
    i = 0
    k_sorted = []
    # 每k个元素进行一次求和，剩余不足k个元素的求和一次
    while i + k <= len(array):
        k_sorted.append(sum(array[i:i + k]))
        i += k
    if i < len(array):
        k_sorted.append(sum(array[k::]))
    # TODO 对其进行quick sort或者merge sort
    return k_sorted


if __name__ == '__main__':
    jug1 = [13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21, 34, 52, 56, 24, 78, 32]
    jug2 = jug1[::-1]
    print(jug_quick_sort(jug1[::], jug2[::]))
    print(k_sort(jug1, 7))
