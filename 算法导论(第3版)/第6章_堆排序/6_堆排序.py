import math


def max_heapify(array, i):
    """
    假设i+1节点的左子二叉树树和右子二叉树都已经是最大堆，函数返回以i+1为根节点的最大堆
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
        if len(array) > 2:
            right_child = array[2 * k]
        else:
            right_child = min(current_node, left_child) - 1
        maxmum_node = max(current_node, left_child, right_child)
        if left_child == maxmum_node:
            array[k - 1], array[2 * k - 1] = left_child, current_node
            return max_heapify(array, 2 * k - 1)
        elif right_child == maxmum_node:
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
    ordered_array = []
    while heap_length > 0:
        array[heap_length - 1], array[0] = array[0], array[heap_length - 1]
        heap_length -= 1
        ordered_array.append(array.pop())
        max_heapify(array, 0)
    return ordered_array


if __name__ == '__main__':
    A = [0, 5, 100, 1, 2, 3, 4]
    print(heap_sort(A))
