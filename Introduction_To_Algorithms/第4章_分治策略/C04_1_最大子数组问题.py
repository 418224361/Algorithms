import math


def find_max_crossing_subarray(array, low, mid, high):
    """
    查找跨越列表array[low:high]的中点mid的最大子数组
    :return:左端点索引,右端点索引,最大和
    """
    if max(array) < 0:
        return array.index(max(array)), array.index(max(array)) + 1, max(array)
    elif min(array) >= 0:
        return 0, len(array) - 1, sum(array)
    else:
        i = j = mid
        left_max = right_max = mid  # 记录最大子列的位置索引
        left_sum_max = right_sum_max = array[mid]
        left_sum = right_sum = array[mid]
        while i > low:
            i -= 1
            left_sum += array[i]
            if left_sum >= left_sum_max:
                left_sum_max = left_sum
                left_max = i
        while j < high:
            j += 1
            right_sum += array[j]
            if right_sum >= right_sum_max:
                right_sum_max = right_sum
                right_max = j + 1
        return left_max, right_max, sum(array[left_max: right_max])


def find_max_subarray(array, low=None, high=None):
    """
    序列array[low:high]的最大和子序列，左闭右开
    """
    if low is None and high is None:
        low = 0
        high = len(array)-1
    if high - low <= 1:  # 递归的base条件
        return find_max_crossing_subarray(array, low, low, high)
    mid = math.floor((low + high) / 2)
    left_low, left_high, left_sum = find_max_subarray(array, low, mid)
    right_low, right_high, right_sum = find_max_subarray(array, mid, high)
    cross_low, cross_high, cross_sum = find_max_crossing_subarray(array, low, mid, high)
    max_sum = max(left_sum, right_sum, cross_sum)
    if left_sum == max_sum:
        return left_low, left_high, max_sum
    elif cross_sum == max_sum:
        return cross_low, cross_high, max_sum
    else:
        return right_low, right_high, max_sum


# 练习4.1-2
def lx41_2(array):
    # 暴力法求最大子数组
    max_sum = array[0]
    max_i = 0
    max_j = 0
    for i in range(len(array)):
        for j in range(i, len(array)):
            summary = sum(array[i:j + 1])
            if summary > max_sum:
                max_i = i
                max_j = min(j + 1, len(array) - 1)
                max_sum = summary
    return max_i, max_j, max_sum


# 练习4.1-4 允许返回空数组
def lx41_4(array, low, high):
    result = find_max_subarray(array, low, high)
    if result[-1] >= 0:
        return result
    return False


# TODO 4.1-5 线性方法查找最大子数组
# 伪代码
# ITERATIVE-FIND-MAXIMUM-SUBARRAY(A)
#     n = A.length
#     max-sum = -∞
#     sum = -∞
#     for j = 1 to n
#         currentHigh = j
#         if sum > 0
#             sum = sum + A[j]
#         else
#             currentLow = j
#             sum = A[j]
#         if sum > max-sum
#             max-sum = sum
#             low = currentLow
#             high = currentHigh
#     return (low, high, max-sum)


if __name__ == '__main__':
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    B = [-abs(i) for i in A]
    C = [abs(i) for i in A]
    print(find_max_subarray(A[:]))
    print(find_max_subarray(B[:]))
    print(find_max_subarray(C[:]))
    print(lx41_4(B, 0, len(B) - 1))
