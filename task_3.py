""" Напишите функцию для транспонирования матрицы
"""


def transponded(matrix: list[tuple[int]]) -> list[tuple[int]]:
    return list(zip(*matrix))


def matrix_printer(matrix: list[tuple[int]]) -> None:
    for row in matrix:
        print(row)
    print('*' * 10)


matrix = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

matrix_printer(matrix)
matrix_printer(transponded(matrix))
