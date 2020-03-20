import math


def lx12_2(c):
    # 用迭代方法求解超越方程 8*n*n < 64*n*lg n 的整数解
    if c <= 0:
        raise ValueError
    n = 2
    while n < c * math.log2(n):
        n += 1
    return n-1


def lx12_3(c):
    # 用迭代方法求解超越方程 100*n*n > 2^n 的整数解
    if c <= 0:
        raise ValueError
    n = 1
    while math.log2(c)+2*math.log2(n) > n:
        n += 1
    return n


if __name__ == '__main__':
    print(lx12_2(8))
    print(lx12_3(100))
