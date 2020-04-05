import math


def max_heapify(array, i):
    """
    假设i+1节点的左子二叉树和右子二叉树都已经是最大堆，函数返回以i+1为根节点的最大堆
    :param array:待排序的序列
    :param i: i= 0,1,2,...,len(array)-1，是节点在array中的下标，i+1为节点编号1,2,3,...len(array)
    :return:以i+1为根节点的最大堆
    """
    k = i + 1
    if k > math.floor(len(array) / 2):  # 如果是叶节点，停止递归，返回array
        return array
    else:
        current_node = array[k - 1]
        left_child = array[2 * k - 1]
        if 2 * k <= len(array) - 1:
            right_child = array[2 * k]
        else:
            right_child = min(current_node, left_child) - 1
        maximum_node = max(current_node, left_child, right_child)
        if left_child == maximum_node:
            array[k - 1], array[2 * k - 1] = left_child, current_node
            return max_heapify(array, 2 * k - 1)
        elif right_child == maximum_node:
            array[k - 1], array[2 * k] = right_child, current_node
            return max_heapify(array, 2 * k)
        else:
            return array


def build_max_heap(array):
    for i in range(math.floor(len(array) / 2) - 1, -1, -1):
        max_heapify(array, i)
    return array


def heap_sort(array):
    # 并没有实现原址排序，若想实现原址排序，需要链表结构。因为做到max_heapify只对array[:-1]个元素排序
    build_max_heap(array)
    heap_length = len(array)
    local_array = array[::]
    ordered_array = []
    while heap_length > 0:
        local_array[heap_length - 1], local_array[0] = local_array[0], local_array[heap_length - 1]
        heap_length -= 1
        ordered_array.append(local_array.pop())
        max_heapify(local_array, 0)
    return ordered_array


def heap_max(array):
    new_array = heap_sort(array)
    return new_array[0]


def heap_extract_max(array):
    build_max_heap(array)
    if len(array) < 1:
        return ValueError
    else:
        maximum = array[0]
        array[len(array) - 1], array[0] = array[0], array[len(array) - 1]
        array = array[:-1]
        build_max_heap(array)
        return maximum, array


def heap_increase_key(array, i, key):
    if key < array[i]:
        raise ValueError
    else:
        # 若大于父节点，则和父节点交换
        while array[math.floor((i + 1) / 2 - 1)] < key and i > 0:
            array[math.floor((i + 1) / 2 - 1)], array[i] = key, array[math.floor((i + 1) / 2 - 1)]
            i = math.floor((i + 1) / 2 - 1)
        return array


def max_heap_insert(array, key):
    array.append(key)
    return heap_increase_key(array, len(array) - 1, key)


def heap_delete(array, i):
    build_max_heap(array)
    if array[i] > array[-1]:
        array[i] = array[-1]
        max_heapify(array, i)
        return array[:-1]
    else:
        array[i] = array[-1]
        return array[:-1]


# 思考题6-1，用插入法建堆
def build_max_heap_prime(array):
    ordered_array = []
    for i in range(len(array)):
        max_heap_insert(ordered_array, array[i])
    return ordered_array


if __name__ == '__main__':
    fig6_5 = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    print(heap_increase_key(fig6_5[:], len(fig6_5) - 1, 15))
    list_65_8 = [15, 7, 9, 1, 2, 3, 8]
    print(heap_delete(list_65_8[:], 4))
    fig6_5 = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    print(max_heap_insert(fig6_5[:], 15))
    a = [1, 2, 3, 4, 5, 6]
    print(build_max_heap_prime(a))
    print(build_max_heap(a))
