#!/usr/bin/python3
"""Rotate a 2D matrix"""
from typing import List


def rotate_2d_matrix(matrix: List) -> None:
    """
    Rotates a 2D matrix

    Args:
    """

    print([list(reversed(col)) for col in zip(*matrix)])
    return [list(reversed(col)) for col in zip(*matrix)]
