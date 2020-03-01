import random


def partition(array, p, r):
    """
    对数组array[p:r]进行分割，不含r
    :return: 返回分割后的数组以及主元(pivot element)
    """
    if p > r:
        return ValueError
    else:
        x = array[r - 1]
        i = p - 1
        for j in range(p, r - 1):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[r - 1] = array[r - 1], array[i + 1]
    return array, i + 1


def randomized_partition(array, p, r):
    """
    对数组array[p,r]进行随机分割，不含r
    :return: 返回分割后的数组以及主元(pivot element)
    """
    i = random.randrange(p, r)  # randrange不包含r
    array[i], array[r - 1] = array[r - 1], array[i]
    return partition(array, p, r)


def quick_sort(array):
    if len(array) == 1:
        return array
    else:
        array, q = partition(array, 0, len(array))
        # 一个不太好预防的边界条件
        if q == 0:
            return array
        else:
            left_array = quick_sort(array[0:q])
            right_array = quick_sort(array[q:len(array)])
            left_array.extend(right_array)
        return left_array


def randomized_quick_sort(array):
    if len(array) == 1:
        return array
    else:
        array, q = randomized_partition(array, 0, len(array))
        # 一个不太好预防的边界条件
        if q == 0:
            return array
        else:
            left_array = quick_sort(array[0:q])
            right_array = quick_sort(array[q:len(array)])
            left_array.extend(right_array)
        return left_array


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


def hoare_quick_sort(array):
    if len(array) == 1:
        return array
    else:
        array, q = hoare_partition(array, 0, len(array))
        # 一个不太好预防的边界条件
        if q == 0:
            return array
        else:
            left_array = quick_sort(array[0:q])
            right_array = quick_sort(array[q:len(array)])
            left_array.extend(right_array)
        return left_array


def partition_prime(array, p, r):
    """
    对数组array[p:r]进行分割，不含r。 p<=q<=t<=r 针对array中相同元素进行处理。处理后的序列分为三部分:
    array[p, q]的元素小于pivot
    array[q, t+1]的元素相等(不一定等于pivot)
    array[t+1, r]的元素大于pivot
    :return: 返回分割后的数组以及q, t
    """
    if p > r:
        return ValueError
    else:
        x = array[r - 1]
        i = p - 1
        k = p - 1
        for j in range(p, r - 1):
            if array[j] == x:
                k += 1
                array[k], array[j] = array[j], array[k]
            elif array[j] < x:
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


def partition_prime_(array, p, r):
    """
    'partition_prime函数的另外一种实现'
    对数组array[p:r]进行分割，不含r。 p<=q<=t<=r 针对array中相同元素进行处理。处理后的序列分为三部分:
    array[p, q]的元素小于pivot
    array[q, t+1]的元素相等(不一定等于pivot)
    array[t+1, r]的元素大于pivot
    :return: 返回分割后的数组以及q, t
    """
    if p > r:
        return ValueError
    else:
        x = array[r - 1]
        i = p - 1
        k = p - 1
        for j in range(p, r - 1):
            if array[j] == x:
                k += 1
                array[k], array[j] = array[j], array[k]
            elif array[j] < x:
                small = array[j]
                notless = array[i]
                big = array[k]
                # 下面两行的顺序不能颠倒
                array[k] = notless
                array[i] = small
                array[j] = big
        array[k + 1], array[r - 1] = array[r - 1], array[k + 1]
    return array, i + 1, k + 1


def randomized_partition_prime(array, p, r):
    """
    对数组array[p,r]进行随机分割，不含r。p<=q<=t<=r 针对array中相同元素进行处理。处理后的序列分为三部分:
    array[p, q]的元素小于pivot
    array[q, t+1]的元素相等(不一定等于pivot)
    array[t+1, r]的元素大于pivot
    :return: 返回分割后的数组以及主元(pivot element)
    """
    i = random.randrange(p, r)  # randrange不包含r
    array[i], array[r - 1] = array[r - 1], array[i]
    return partition_prime(array, p, r)


def quick_sort_prime(array):
    """
    使用随机pivot对array划分并排序。对具有相同元素的数组进行优化
    """
    if len(array) <= 1:
        return array
    else:
        array, q, t = randomized_partition_prime(array, 0, len(array))
        smaller_array = quick_sort_prime(array[:q])
        equal_array = quick_sort_prime(array[q: t])
        greater_array = quick_sort_prime(array[t:])
        if len(equal_array) == 0:
            smaller_array.extend(greater_array)
            return smaller_array
        elif len(smaller_array) == 0:
            equal_array.extend(greater_array)
            return equal_array
        elif len(greater_array) == 0:
            smaller_array.extend(equal_array)
            return smaller_array
        else:
            smaller_array.extend(equal_array)
            smaller_array.extend(greater_array)
            return smaller_array


if __name__ == '__main__':
    A = [2, 8, 7, 1, 3, 5, 6, 4]
    B = [13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21]
    C = [1, 2, 3, 4, 5, 4, 4, 3]
    D = [1, 1, 1, 1, 1]
    print(quick_sort(A[:]))
    print(randomized_quick_sort(A[:]))
    print(hoare_quick_sort(A[:]))
    print(randomized_partition_prime(A[:], 0, len(A)))
    print(randomized_partition_prime(C[:], 0, len(C)))
    print(randomized_partition_prime(D[:], 0, len(D)))
    print(quick_sort_prime(A[:]))
    print(quick_sort_prime(B[:]))
    print(quick_sort_prime(C[:]))
    print(quick_sort_prime(D[:]))

    # 思考题7-1
    """
    x=13
    
    j=12, i=-1, a = [13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21], 
    
    j=11, i=0, a = [6, 19, 9, 5, 12, 8, 7, 4, 11, 2, 13, 21]
    
    j=10, i=1 ,a = [6, 2, 9, 5, 12, 8, 7, 4, 11, 19, 13, 21]
    
    j=10, i=1 ,a = [6, 2, 9, 5, 12, 8, 7, 4, 11, 19, 13, 21]
    
    j=9, i = 9
    """
