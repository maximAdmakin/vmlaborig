import copy

import numpy as np


def det(a, s):
    idx_col = s

    rows = len(a)
    for i in range(rows):
        _ = a[i].pop(idx_col)
    return np.linalg.det(a)


def gaussMethod(matrix, size):
    matrix1 = copy.deepcopy(matrix)
    print("Первоначальный вид матрицы:\n")
    for i in matrix1:
        print(*i)
    print("\n")
    x = [0 for i in range(size)]
    for globalStep in range(size):
        for i in range(globalStep, size):
            buffer = matrix[i][globalStep]
            for i1 in range(globalStep, size+1):
                matrix[i][i1] = matrix[i][i1]/buffer
        for i1 in range(globalStep + 1, size):
            for i2 in range(size + 1):
                matrix[i1][i2] = matrix[i1][i2] - matrix[globalStep][i2]

    x[size - 1] = matrix[size - 1][size]

    for i in reversed(range(0, size-1)):
        buffer = 0.0
        for deep in range(i+1, size):
            buffer = buffer + (matrix[i][deep] * x[deep])
        x[i] = matrix[i][size] - buffer

    r = [0 for i in range(size)]

    for i in range(size):
        buffer = 0.0
        for deep in range(size):
            buffer = buffer + (matrix[i][deep] * x[deep])
        r[i] = matrix[i][size] - buffer

    return matrix, r, x, det(matrix1, size)