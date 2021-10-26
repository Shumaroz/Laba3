from sys import stdin
from copy import deepcopy
import numpy

class Matrix:
    def __init__(self, list_of_lists):
        self.matrix = deepcopy(list_of_lists)

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)

    def __getitem__(self, idx):
        return self.matrix[idx]
    # Сравнение матриц
    # Матрица 1 больше матрицы 2
    def __gt__(self, other):
        return numpy.linalg.det(self.matrix) > numpy.linalg.det(other.matrix)
    # Матрица 1 меньше матрицы 2
    def __lt__(self, other):
        return numpy.linalg.det(self.matrix) < numpy.linalg.det(other.matrix)
    # Матрица 1 равна матрице 2
    def __eq__(self, other):
        return numpy.linalg.det(self.matrix) == numpy.linalg.det(other.matrix)
    # Сложение матриц
    def __add__(self, other):
        other = Matrix(other)
        result = []
        numbers = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                summa = other[i][j] + self.matrix[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.matrix):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)
    # Умножение матриц
    def __mul__(self, other):
        result = Matrix([[0,0],[0,0]])
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[0])):
                for k in range(len(other.matrix)):
                    result[i][j] += self[i][k] * other[k][j]
        return result

m1 = Matrix([[1,1],[2,2]])
m2 = Matrix([[1,2],[3,4]])
if m1 > m2:
    print("m1 greater than m2")
elif m1 == m2:
    print("Equal")
else:
    print("m2 greater than m1")

print("\nSum:")
print(m1 + m2)
print("\nMult:")
print(m1 * m2)