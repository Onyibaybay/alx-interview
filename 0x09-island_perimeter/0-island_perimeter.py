#!/usr/bin/python3
"""
Module that calculates the perimeter of an island represented in a grid.
The grid is a list of list of integers where 0 represents water and 1
represents land. Each cell in the grid is a square with a side length of 1,
and the cells are connected horizontally or vertically (not diagonally).
The grid is rectangular and completely surrounded by water.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
        grid (list of list of int): A list of list of integers representing
        the grid. 0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Add 4 for each land cell
                perimeter += 4

                # Subtract 2 for each adjacent land cell (top and left)
                if i > 0 and grid[i-1][j] == 1:  # check top
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:  # check left
                    perimeter -= 2

    return perimeter