"""
Напишите алгоритм, реализующий следующее условие: если элемент матрицы MxN равен
нулю, то весь столбец и вся строка обнуляется
"""
import random
from typing import List

random.seed(0)


def init_matrix(m: int, n: int) -> List[List[int]]:
    return [[random.randrange(-5, 5, 1) for _ in range(m)] for _ in range(n)]


def check_by_null(m: List[List[int]]) -> List[List[int]]:
    _matrix = []
    empty_col = []
    for x in range(len(m)):
        row = []
        for y in range(len(m[0])):
            if m[x][y] == 0:
                row = [0 for _ in range(len(m[0]))]
                empty_col.append(y)
                break
            else:
                row.append(m[x][y])
        _matrix.append(row)

    for x in range(len(m)):
        for y in range(len(m[0])):
            if y in empty_col:
                _matrix[x][y] = 0

    return _matrix


def print_matrix(m: List[List[int]]) -> None:
    print("\n".join([str(data) for data in m]))


matrix = init_matrix(5, 7)
print_matrix(matrix)

print()

changed_matrix = check_by_null(matrix)
print_matrix(changed_matrix)
