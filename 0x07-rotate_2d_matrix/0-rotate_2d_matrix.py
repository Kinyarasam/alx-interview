#!/usr/bin/python3
"""Rotate a 2D matrix"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix

    Args:
        matrix (List): the 2D matrix
    """
    # print([list(reversed(col)) for col in zip(*matrix)])
    # return [list(reversed(col)) for col in zip(*matrix)]
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
