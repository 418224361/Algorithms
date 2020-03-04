def insertion_sort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key
    return array


# 2.1-2
def insertion_sort_not_increase(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] < key:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key
    return array


# 2.1-3
def lx_21_3(array, v):
    # 找到array中值为v的元素的下标，如果没有返回nil
    result = False
    i = 0
    while i < len(array):
        if array[i] == v:
            result = True
            break
        i += 1
    return result


# 2.1-4
def lx_21_4(array1, array2):
    # 两个n位二进制整数相加，生成一个n+1位二进制整数
    carry = 0
    n = len(array1)
    array = []
    for i in range(n):
        position = n - i - 1
        carry, digit = divmod(array1[position] + array2[position] + carry, 2)
        array.append(digit)
    if carry == 1:
        array.append(carry)
    return array[::-1]


if __name__ == '__main__':
    a = [31, 41, 59, 26, 41, 58]
    print(insertion_sort(a))
    print(insertion_sort_not_increase(a))
    print(lx_21_3(a, 41))
    array1 = [1, 0, 0, 1, 1]
    array2 = [0, 0, 1, 1, 1]
    print(lx_21_4(array1, array2))
