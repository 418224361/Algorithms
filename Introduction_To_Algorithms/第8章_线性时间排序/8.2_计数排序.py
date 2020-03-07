import math


def counting_sort(array):
    """
    当a的元素是非负整数时可以使用计数排序，尤其当 max(a) 远远小于 n=len(a) 时，可以获得Theta(n)的时间复杂度
    """
    k = max(array) + 1
    c = [0] * k
    b = [0] * len(array)
    # c[i]等于array中值为i的元素的数量
    for j in range(len(array)):
        c[array[j]] += 1
    # 累计小于等于i的元素的数量，赋值给c[i]
    for i in range(1, k):
        c[i] += c[i - 1]
    for j in range(len(array) - 1, -1, -1):
        b[c[array[j]] - 1] = array[j]
        c[array[j]] -= 1
    return b


# 练习题8.2-4
def lx82_4(array, a, b):
    """
    对array进行预处理，使其能够在常数时间内返回落在区间[a,b]内的元素个数。预处理的时间应为Theta(n)
    array的元素应为非负整数
    """
    k = max(array) + 1
    c = [0] * k
    for j in range(len(array)):
        c[array[j]] += 1
    for i in range(1, k):
        c[i] += c[i-1]
    return c[math.floor(b)] - c[math.floor(a-1)]


if __name__ == '__main__':
    A = [2, 8, 7, 1, 3, 5, 6, 4]
    B = [13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21]
    C = [1, 2, 3, 4, 5, 6, 7, 4, 4, 3]
    D = [1, 1, 1, 1, 1]
    E = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]

    print(counting_sort(A))
    print(counting_sort(B))
    print(counting_sort(C))
    print(counting_sort(D))
    print(counting_sort(E))

    print(lx82_4(A, 3, 5))
