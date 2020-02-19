# 矩阵乘法(平凡算法)
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


def matrix_multipy_trivil(A, B):
    # 对输入矩阵格式进行检查
    if len(A) == 0:  # 确保A矩阵行数不为0
        raise ValueError('Null matrix {}'.format(A))
    elif len(B) == 0:  # 确保B矩阵行数不为0
        raise ValueError('Null matrix {}'.format(B))
    elif len(A[0]) == 0:  # 确保A矩阵列数不为0
        raise ValueError('{} matrix column is Null'.format(A))
    elif len(B[0]) == 0:  # 确保B矩阵列数不为0
        raise ValueError('{} matrix column is Null'.format(A))
    a_row_number = len(A)
    a_column_number = len(A[0])
    b_row_number = len(B)
    b_column_number = len(B[0])
    for row in range(a_row_number):
        if len(A[row]) != a_column_number:
            raise ValueError('{}矩阵第{}行列数有误'.format(A, row))
    for row in range(b_row_number):
        if len(B[row]) != b_column_number:
            raise ValueError('{}矩阵第{}行列数有误'.format(B, row))
    if a_column_number != b_row_number:  # A的列数要等于B的行数
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


print(A)
print(B)
C = matrix_multipy_trivil(A, B)
print(C)
