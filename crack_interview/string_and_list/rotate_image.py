"""
Имеется изображение, представленное матрицей N x N, каждый пиксель имеет 4 байта.
Напишите метод для поворота изображения на 90 градусов. Удастся ли вам выполнить эту
операцию "на месте"?
"""
import random
from typing import List

random.seed(0)


class Pixel:
    some_data: int

    def __init__(self):
        self.some_data = random.randrange(-5, 5, 1)

    def __repr__(self):
        return str(self.some_data)


class Matrix:
    size: int
    data: List[List[Pixel]]

    def __init__(self, size: int, data=None):
        self.size = size
        if data:
            self.data = data
        else:
            self.__init_matrix()

    def __init_matrix(self):
        payload = []
        row = []
        for x in range(self.size):
            for y in range(self.size):
                row.append(Pixel())
            payload.append(row)
            row = []
        self.data = payload

    def __len__(self):
        return self.size

    def __getitem__(self, key):
        return self.data[key]

    def __repr__(self):
        return "\n".join([str(pixel) for pixel in self.data])


def rotate(m: Matrix):
    data = [[m[j][i] for j in range(len(m))] for i in range(len(m) - 1, -1, -1)]
    return Matrix(size=len(m), data=data)


matrix = Matrix(size=5)
print(matrix)

print()

new_matrix = rotate(matrix)
print(new_matrix)
