#!/usr/bin/python3
"""
This is a Python script that generates a Pascal's triangle of a specified \
size using a function called pascal_triangle. The triangle is printed to \
the console using a helper function called print_triangle.
"""
from typing import List


def pascal_triangle(n: int) -> List[List[int]]:
    """
    Returns a list of lists of integers representing the Pascal's
    triangle of n.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        List[List[int]]: A list of lists of integers representing
        the Pascal's triangle
    """
    # Initialize an empty list to store the rowa of the triangle
    result = []

    # Iterate through each row in the triangle
    for i in range(n):
        # Initialize an empty list to store the elements in the row
        row = []

        # Iterate through each element in the row
        for j in range(i + 1):
            """If the element is at the beginning or end of the row, \
set its value to 1"""
            if j == 0 or j == i:
                row.append(1)
            # Otherwise, set its value to the sum of the values in
            # the previous row at position j and j - 1
            else:
                row.append(result[i - 1][j] + result[i - 1][j - 1])

        # Add the row to the result list
        result.append(row)

    # Return the result list
    return result
