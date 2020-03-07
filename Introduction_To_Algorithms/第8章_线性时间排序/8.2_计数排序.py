def counting_sort(a):
    """
    当a的元素是非负整数时可以使用计数排序，尤其当 max(a) 远远小于 n=len(a) 时，可以获得O(n)的时间复杂度
    """
    k = max(a)+1
    c = [0] * k
    b = [0] * len(a)
    # c[i]等于array中值为i的元素的数量
    for j in range(len(a)):
        c[a[j]] += 1
    # 累计小于等于i的元素的数量，赋值给c[i]
    for i in range(1, k):
        c[i] += c[i - 1]
    for j in range(len(a)-1, -1, -1):
        b[c[a[j]]-1] = a[j]
        c[a[j]] -= 1
    return b


if __name__ == '__main__':
    A = [2, 8, 7, 1, 3, 5, 6, 4]
    B = [13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21]
    C = [1, 2, 3, 4, 5, 6, 7, 4, 4, 3]
    D = [1, 1, 1, 1, 1]

    print(counting_sort(A))
    print(counting_sort(B))
    print(counting_sort(C))
    print(counting_sort(D))
