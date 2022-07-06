#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for row in matrix:
        for col in matrix:
            return map(lambda x: x**2, matrix)
