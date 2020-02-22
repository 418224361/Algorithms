import math


def get_matrix_size(matrix):
    """
    获取矩阵的行数和列数
    ！！注意，在对矩阵的情况不了解时，需要首先执行check_matrix(A)，检查其行数列数和元素数是否合法
    :param matrix:矩阵A
    :return: 数组形式的行数，列数
    """
    return len(matrix), len(matrix[0])


def check_matrix(matrix, empty_matrix=False):
    """
    检查矩阵的行列和元素是否有值
    :param matrix: 待检查矩阵
    :param empty_matrix: 如果是空矩阵，请置为True，否则默认False
    :return: 若检查无误，返回True，否则抛出异常
    """
    if empty_matrix is True:
        return True
    elif len(matrix) == 0:  # 确保A矩阵行数不为0
        raise ValueError('{}矩阵为空'.format(matrix))
    elif len(matrix[0]) == 0:  # 确保A矩阵列数不为0
        raise ValueError('{}矩阵的列为空'.format(matrix))
    row_number, column_number = get_matrix_size(matrix)
    for row in range(row_number):
        if len(matrix[row]) != column_number:
            raise ValueError('{}矩阵第{}行列数有误'.format(matrix, row))
    return True


def matrix_multipy(A, B):
    # 检查矩阵非空，各个位置均有元素填充
    check_matrix(A, empty_matrix=False)
    check_matrix(A, empty_matrix=False)

    # 获取矩阵规模
    a_row_number, a_column_number = get_matrix_size(A)
    b_row_number, b_column_number = get_matrix_size(B)

    # 检查A的列数是否等于B的行数
    if a_column_number != b_row_number:
        raise ValueError('{}的列不等于{}的行数'.format(A, B))

    # 计算矩阵乘积
    matrix = []
    for i in range(a_row_number):  # A的第i+1行
        temp_array = [0] * b_column_number
        for j in range(b_column_number):  # A的第i+1行的第j+1列
            total = 0
            for k in range(a_column_number):  # A的第k+1列(同时也是B的第k+1行)
                total += A[i][k] * B[k][j]
            temp_array[j] = total
        matrix.append(temp_array)
    return matrix


def matrix_fillup(matrix):
    """
    对任意矩阵进行检查，并用0补齐为n阶方阵，其中n是2的整数次幂。
    :param matrix: 待补齐的矩阵
    :return: 补齐后的方阵, 原始行数，原始列数，n
    """
    # 检查矩阵非空，各个位置均有元素填充
    check_matrix(matrix, empty_matrix=False)

    # 计算目标行列数n
    row_number, columum_number = get_matrix_size(matrix)
    if row_number >= columum_number:
        n = 2 ** (math.ceil(math.log2(row_number)))
    else:
        n = 2 ** (math.ceil(math.log2(columum_number)))

    # 用0补齐为n*n阶方阵。先补齐现有行的列数，再补齐剩余行数。
    row_gap = n - row_number
    columum_gap = n - columum_number
    for i in range(row_number):
        matrix[i].extend([0] * columum_gap)
    for i in range(row_gap):
        matrix.append([0] * n)
    return matrix, row_number, columum_number, n


def sub_matrix(matrix):
    matrix, row_number, columum_number, n = matrix_fillup(matrix)
    half_n = int(n/2)
    temp_array = [0] * int(n/2)
    m11 = [temp_array[:] for t in range(half_n)]
    m12 = [temp_array[:] for t in range(half_n)]
    m21 = [temp_array[:] for t in range(half_n)]
    m22 = [temp_array[:] for t in range(half_n)]
    for i in range(half_n):
        for j in range(half_n):
            m11[i][j] = matrix[i][j]

    for i in range(half_n):
        for j in range(half_n):
            m12[i][j] = matrix[i][j+half_n]

    for i in range(half_n):
        for j in range(half_n):
            m21[i][j] = matrix[i+half_n][j]

    for i in range(half_n):
        for j in range(half_n):
            m22[i][j] = matrix[i+half_n][j+half_n]

    return m11, m12, m21, m22



def strassen(A, B):
    pass


if __name__ == '__main__':
    row_A1 = [1, 4, 7]
    row_A2 = [2, 5, 8]
    row_A3 = [3, 6, 9]

    row_B1 = [10, 13]
    row_B2 = [11, 14]
    row_B3 = [12, 15]

    A = []
    B = []
    A.append(row_A1)
    A.append(row_A2)
    A.append(row_A3)
    B.append(row_B1)
    B.append(row_B2)
    B.append(row_B3)

    # print(A)
    # print(B)
    # C = matrix_multipy(A, B)
    # print(C)
    print(matrix_fillup(B))
    print(sub_matrix(B))