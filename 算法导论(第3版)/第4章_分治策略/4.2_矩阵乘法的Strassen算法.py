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


def matrix_minus(A, B, check=False):
    if check is True:
        # 检查矩阵非空，各个位置均有元素填充
        check_matrix(A, empty_matrix=False)
        check_matrix(B, empty_matrix=False)

    # 获取矩阵规模
    a_row_number, a_column_number = get_matrix_size(A)
    b_row_number, b_column_number = get_matrix_size(B)

    # 检查A的行列数是否等于B的行列数
    if a_column_number != b_column_number or a_row_number != b_row_number:
        raise ValueError('{}的行列不等于{}的行列数'.format(A, B))

    # 计算矩阵加法
    temp_array = [0] * a_column_number
    matrix = [temp_array[:] for t in range(a_row_number)]
    for i in range(a_row_number):
        for j in range(a_column_number):
            matrix[i][j] = A[i][j] - B[i][j]
    return matrix


def matrix_add(A, B, check=False):
    if check is True:
        # 检查矩阵非空，各个位置均有元素填充
        check_matrix(A, empty_matrix=False)
        check_matrix(B, empty_matrix=False)

    # 获取矩阵规模
    a_row_number, a_column_number = get_matrix_size(A)
    b_row_number, b_column_number = get_matrix_size(B)

    # 检查A的行列数是否等于B的行列数
    if a_column_number != b_column_number or a_row_number != b_row_number:
        raise ValueError('{}的行列不等于{}的行列数'.format(A, B))

    # 计算矩阵加法
    temp_array = [0] * a_column_number
    matrix = [temp_array[:] for t in range(a_row_number)]
    for i in range(a_row_number):
        for j in range(a_column_number):
            matrix[i][j] = A[i][j] + B[i][j]
    return matrix


def matrix_multiply(A, B, check=False):
    if check is True:
        # 检查矩阵非空，各个位置均有元素填充
        check_matrix(A, empty_matrix=False)
        check_matrix(B, empty_matrix=False)

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


def matrix_fillup(matrix, check=True):
    """
    对任意矩阵进行检查，并用0补齐为n阶方阵，其中n是2的整数次幂。
    :param matrix: 待补齐的矩阵
    :return: 补齐后的方阵, 原始行数，原始列数，n
    """
    if check is True:
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
    half_n = int(n / 2)
    temp_array = [0] * int(n / 2)
    m11 = [temp_array[:] for t in range(half_n)]
    m12 = [temp_array[:] for t in range(half_n)]
    m21 = [temp_array[:] for t in range(half_n)]
    m22 = [temp_array[:] for t in range(half_n)]
    for i in range(half_n):
        for j in range(half_n):
            m11[i][j] = matrix[i][j]

    for i in range(half_n):
        for j in range(half_n):
            m12[i][j] = matrix[i][j + half_n]

    for i in range(half_n):
        for j in range(half_n):
            m21[i][j] = matrix[i + half_n][j]

    for i in range(half_n):
        for j in range(half_n):
            m22[i][j] = matrix[i + half_n][j + half_n]

    return m11, m12, m21, m22, row_number, columum_number, n


def _strassen(A, B):
    if len(A) == 1:
        return [[A[0][0] * B[0][0]]]
    else:
        a11, a12, a21, a22, a_row_number, a_columum_number, n = sub_matrix(A)
        b11, b12, b21, b22, b_row_number, b_columum_number, n = sub_matrix(B)
        s1 = matrix_minus(b12, b22)
        s2 = matrix_add(a11, a12)
        s3 = matrix_add(a21, a22)
        s4 = matrix_minus(b21, b11)
        s5 = matrix_add(a11, a22)
        s6 = matrix_add(b11, b22)
        s7 = matrix_minus(a12, a22)
        s8 = matrix_add(b21, b22)
        s9 = matrix_minus(a11, a21)
        s10 = matrix_add(b11, b12)

        p1 = _strassen(a11, s1)
        p2 = _strassen(s2, b22)
        p3 = _strassen(s3, b11)
        p4 = _strassen(a22, s4)
        p5 = _strassen(s5, s6)
        p6 = _strassen(s7, s8)
        p7 = _strassen(s9, s10)

        c11 = matrix_add(matrix_minus(matrix_add(p5, p4), p2), p6)
        c12 = matrix_add(p1, p2)
        c21 = matrix_add(p3, p4)
        c22 = matrix_minus(matrix_minus(matrix_add(p5, p1), p3), p7)

        temp_array = [0] * n
        matrix = [temp_array[:] for t in range(n)]
        half_n = int(n / 2)

        for i in range(half_n):
            for j in range(half_n):
                matrix[i][j] = c11[i][j]

        for i in range(half_n):
            for j in range(half_n):
                matrix[i][j + half_n] = c12[i][j]

        for i in range(half_n):
            for j in range(half_n):
                matrix[i + half_n][j] = c21[i][j]

        for i in range(half_n):
            for j in range(half_n):
                matrix[i + half_n][j + half_n] = c22[i][j]
        return matrix


def strassen(A, B):
    a_row_number, a_column_number = get_matrix_size(A)
    b_row_number, b_column_number = get_matrix_size(B)
    c = _strassen(A, B)
    if c[-1][-1] == 0:  # 说明有0填充
        c = c[:a_row_number]
        for i in range(a_row_number):
            c[i] = c[i][:b_column_number]
        return c
    return c


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

    print('A = {}'.format(A))
    print('B = {}'.format(A))
    print('A * B = {}'.format(matrix_multiply(A, B)))
    print('A * B (by Strassen) = {}'.format(strassen(A, B)))
