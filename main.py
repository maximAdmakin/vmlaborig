from typing import List

import gauss
print("Выберите метод ввода матрицы\n0 - Ввод с клавиатуры\n1 - Ввод из файла")
inputType = int(input("Метод номер: "))

if inputType == 0:
    size = int(input("Введите размерность матрицы: "))
    matrix = [[0 for i in range(size+1)] for j in range(size)]
    i1 = 0
    i2 = 0
    for i1 in range(size):
        for i2 in range(size+1):
            matrix[i1][i2] = float(input(f"Введите значение ячейки matrix[{i1}][{i2}]: "))
    print("\n")
    resultMatrix, resultR, resultX, resultDet = gauss.gaussMethod(matrix, size)
    print(resultMatrix)
    print(resultX)
    print(resultR)
    print(resultDet)


if inputType == 1:
    print("\n")
    fin = open('matrix', 'r')
    a = [line.strip() for line in fin.readlines()]
    size = int(a[0])
    matrix = [[0 for i in range(size + 1)] for j in range(size)]
    a = a[1:]
    for i1 in range(size):
        mass = (a[i1].split())
        for i2 in range(size + 1):
            matrix[i1][i2] = float(mass[i2])
    resultMatrix, resultR, resultX, resultDet = gauss.gaussMethod(matrix, size)
    print("Треугольная матрица:\n")
    for i in resultMatrix:
        print(*i)
    print("\n")

    print("Вектора неизвестных:\n")
    for i in range(size):
        print(f"x{i+1}: {resultX[i]}")
    print("\n")
    print("Вектора невязок:\n")
    for i in range(size):
        print(f"r{i + 1}: {resultR[i]}")
    print("\n")
    print(f"Определитель: {resultDet}")

if inputType == 2:
    print("haha")



