import random
import math
from Algorithms.TailRecursion import tail_call_optimized


# -------------------- 快速排序(基础版本) -------------------
def partition(array, p, r):
    """
    选取array[r-1]为主元(pivot element)，对列表array[p:r]进行原址重排。注意不含r
    :return: 重排后的列表以及主元
    """
    pivot = array[r - 1]
    i = p - 1
    for j in range(p, r-1):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r - 1] = array[r - 1], array[i + 1]
    return array, i + 1


def quick_sort_basic(array, p=None, r=None):
    """
    快速排序的基本版本。从小到大排序。
    待排序的序列为 array[p:r]
    :return: 排序后的array[p:r]
    """
    if p is None and r is None:
        p = 0
        r = len(array)
    if p >= r-1:
        return array
    else:
        array, q = partition(array, p, r)
        quick_sort_basic(array, p, q)
        quick_sort_basic(array, q+1, r)
        return array


# -------------------- 随机选取主元的快速排序 -------------------
def randomized_partition(array, p, r):
    """
    随机选取array[p:r]中的一个元素为主元(pivot element)，对列表array[p:r]进行原址重排。注意不含r
    :return: 重排后的列表以及主元
    """
    i = random.randrange(p, r)  # randrange不包含r
    array[i], array[r - 1] = array[r - 1], array[i]
    return partition(array, p, r)


def randomized_quick_sort(array, p=None, r=None):
    """
    随机选取主元的快速排序。从小到大排序。
    待排序的序列为 array[p:r]
    :return: 排序后的array[p:r]
    """
    if p is None and r is None:
        p = 0
        r = len(array)
    if p >= r - 1:
        return array
    else:
        array, q = randomized_partition(array, p, r)
        quick_sort(array, p, q)
        quick_sort(array, q, r)
        return array


# -------------------- 思考题7-1，快速排序的最初版本(Hoare) -------------------
def hoare_partition(array, p, r):
    pivot = array[p]
    i = p
    j = r - 1
    while True:
        while array[j] > pivot:
            j -= 1
        while array[i] < pivot:
            i += 1
        if i < j:
            array[i], array[j] = array[j], array[i]
        else:
            return array, j


def hoare_quick_sort(array, p=None, r=None):
    """
    快速排序的最初版本Hoare排序。从小到大排序。
    待排序的序列为 array[p:r]
    :return: 排序后的array[p:r]
    """
    if p is None and r is None:
        p = 0
        r = len(array)
    if p >= r - 1:
        return array
    else:
        array, q = randomized_partition(array, p, r)
        quick_sort(array, p, q)
        quick_sort(array, q, r)
        return array


# -------------------- 思考题7-2，快速排序优化：针对相同元素值的快速排序 -------------------
def _partition_prime(array, p, r):
    """
    选取array[r-1]为主元(pivot element)，对列表array[p:r]进行原址重排。注意不含r
    重排后的序列分为三部分(p<=q<=t<=r):
    array[p:q]的元素小于pivot
    array[q:t+1]的元素等于pivot
    array[t+1:r]的元素大于pivot
    :return: 排序后的array[p:r]以及q, t
    """
    pivot = array[r - 1]
    i = p - 1
    k = p - 1
    for j in range(p, r - 1):
        if array[j] == pivot:
            k += 1
            array[k], array[j] = array[j], array[k]
        elif array[j] < pivot:
            if k == i:  # 此时还没有和pivot相等的元素
                i += 1
                k += 1
                array[i], array[j] = array[j], array[i]
            else:
                i += 1
                k += 1
                # 按照j->i->t->j的顺序交换数值
                small = array[j]
                equ = array[i]
                big = array[k]
                array[i] = small
                array[k] = equ
                array[j] = big
    array[k + 1], array[r - 1] = array[r - 1], array[k + 1]
    return array, i + 1, k + 1


def randomized_partition_prime(array, p, r):
    """
    随机选取array[p:r]中一个元素为主元(pivot element)，对列表array[p:r]进行原址重排。注意不含r
    重排后的序列分为三部分(p<=q<=t<=r):
    array[p:q]的元素小于pivot
    array[q:t+1]的元素等于pivot
    array[t+1:r]的元素大于pivot
    :return: 排序后的array[p:r]以及q, t
    """
    i = random.randrange(p, r)  # randrange不包含r
    array[i], array[r - 1] = array[r - 1], array[i]
    return _partition_prime(array, p, r)


def randomized_quick_sort_prime(array, p=None, r=None):
    """
    随机选取主元的快速排序，并针对具有相同元素场景进行优化。从小到大排序。
    待排序的序列为 array[p:r]
    :return: 排序后的array[p:r]
    """
    if p is None and r is None:
        p = 0
        r = len(array)
    if p >= r - 1:
        return array
    else:
        array, q, t = randomized_partition_prime(array, p, r)
        randomized_quick_sort_prime(array, p, q)
        randomized_quick_sort_prime(array, t+1, r)
        return array


# -------------------- 思考题7-4，快速排序优化：减小栈深度的伪尾递归 -------------------
def pseudo_tail_recursion_quick_sort(array, p=None, r=None):
    """
    伪尾递归快速排序，递归深度lg(r-p+1)
    注意！不是真正的尾递归！
    :return: 排序后的array[p:r]
    """
    if p is None and r is None:
        p = 0
        r = len(array)
    while p < r:
        array, q = partition(array, p, r)
        if q < math.floor((p + r - 1) / 2):
            pseudo_tail_recursion_quick_sort(array, p, q)
            p = q + 1
        else:
            pseudo_tail_recursion_quick_sort(array, q+1, r)
            r = q
    return array


# -------------------- 思考题7-5，快速排序优化：三元素随机主元+伪尾递归+针对相同元素的优化 -------------------
def three_median_partition(array, p, r, n=3):
    """
    从列表 array[p:r] 中随机选出3个元素，然后取中位数作为pivot element
    """
    if len(array[p:r]) > 3:
        rand_entries = sorted(random.sample(array[p:r], k=n))
        median = rand_entries[1]
        array[r - 1], array[array.index(median)] = array[array.index(median)], array[r - 1]
    return _partition_prime(array, p, r)


def quick_sort(array, p=None, r=None):
    """
    原则上性能最优的快速排序
    使用三元素生成随机pivot对array划分并排序。对具有相同元素的数组进行优化
    p<=q<=t<=r
    递归深度小于等于lg((r-p+1)-(t-q+1))
    """
    if p is None and r is None:
        p = 0
        r = len(array)
    array, q, t = three_median_partition(array, p, r)
    pseudo_tail_recursion_quick_sort(array, p, q)
    pseudo_tail_recursion_quick_sort(array, t, r)
    return array


# 一个尾递归的例子
@tail_call_optimized
def tail_fib(n, acc1=0, acc2=1):
    if n == 0:
        return acc1
    else:
        return tail_fib(n - 1, acc2, acc1 + acc2)


if __name__ == '__main__':
    A = [2, 8, 7, 1, 3, 5, 6, 4]
    B = [13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21]
    C = [1, 2, 3, 4, 5, 6, 7, 4, 4, 3]
    D = [1, 1, 1, 1, 1]

    print(quick_sort_basic(A[:]))
    print(quick_sort_basic(B[:]))
    print(quick_sort_basic(C[:]))
    print(quick_sort_basic(D[:]))

    print(randomized_quick_sort(A[:]))
    print(randomized_quick_sort(B[:]))
    print(randomized_quick_sort(C[:]))
    print(randomized_quick_sort(D[:]))

    print(hoare_quick_sort(A[:]))
    print(hoare_quick_sort(B[:]))
    print(hoare_quick_sort(C[:]))
    print(hoare_quick_sort(D[:]))

    print(randomized_quick_sort_prime(A[:]))
    print(randomized_quick_sort_prime(B[:]))
    print(randomized_quick_sort_prime(C[:]))
    print(randomized_quick_sort_prime(D[:]))

    print(pseudo_tail_recursion_quick_sort(A[:]))
    print(pseudo_tail_recursion_quick_sort(B[:]))
    print(pseudo_tail_recursion_quick_sort(C[:]))
    print(pseudo_tail_recursion_quick_sort(D[:]))

    print(quick_sort(A[:]))
    print(quick_sort(B[:]))
    print(quick_sort(C[:]))
    print(quick_sort(D[:]))

    print(tail_fib(10000))

    # 思考题7-1
    """
    x=13
    
    j=12, i=-1, a = [13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21], 
    
    j=11, i=0, a = [6, 19, 9, 5, 12, 8, 7, 4, 11, 2, 13, 21]
    
    j=10, i=1 ,a = [6, 2, 9, 5, 12, 8, 7, 4, 11, 19, 13, 21]
    
    j=10, i=1 ,a = [6, 2, 9, 5, 12, 8, 7, 4, 11, 19, 13, 21]
    
    j=9, i = 9
    """
