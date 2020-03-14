import random


# 思考题8-4
def jug_partition(red, blue, p, r):
    # 首先从蓝桶中随机选出一个blue_pivot，用其对红桶做partition，同时找出相同的红桶red_pivot，再用red_pivot对蓝桶做partition.
    blue_pivot_index = random.randint(p, r)
    blue_pivot = blue[blue_pivot_index]
    # 对红桶进行partition
    l = p - 1
    j = p
    while j < r:
        if red[j] < blue_pivot:
            l += 1
            red[l], red[j] = red[j], red[l]
        # 当red的第j个元素等于blue_pivot时，放到red最后
        elif red[j] == blue_pivot and j != r - 1:
            red.pop(j)
            red.append(blue_pivot)
            continue
        j += 1
    red.insert(l + 1, blue_pivot)
    red.pop()
    # 对蓝桶进行partition
    m = p - 1
    k = p
    while k < r:
        if blue[k] < blue_pivot:
            m += 1
            blue[m], blue[k] = blue[k], blue[m]
        # 当blue的第m个元素等于blue_pivot时，放到blue最后
        elif blue[k] == blue_pivot and k != r - 1:
            blue.pop(k)
            blue.append(blue_pivot)
            continue
        k += 1
    blue.insert(m + 1, blue_pivot)
    blue.pop()
    if l != m:
        raise IndexError('奇怪')
    return red, blue, l + 1


if __name__ == '__main__':
    jug1 = [13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21]
    jug2 = jug1[::-1]
    print(jug_partition(jug1, jug2, 0, len(jug1)))
