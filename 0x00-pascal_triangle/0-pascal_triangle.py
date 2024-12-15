#!/usr/bin/python3
"""
Module: 0-pascal_triangle

Defines a function pascal_triangle(n) that generates Pascal's triangle
up to the nth row.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
    - n (int): Number of rows to generate

    Returns:
    - list of lists of integers: Pascal's triangle up to the nth row
      Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row

    for i in range(1, n):
        prev_row = triangle[-1]
        current_row = [1]  # First element of the row is always 1

        # Calculate each element in the current row
        for j in range(1, i):
            current_row.append(prev_row[j - 1] + prev_row[j])

        current_row.append(1)  # Last element of the row is always 1
        triangle.append(current_row)

    return triangle
