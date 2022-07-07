#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for row in matrix:
        for col in row:
            print("{:d}".format(col**2))
    print()
