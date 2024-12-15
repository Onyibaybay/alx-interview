#!/usr/bin/python3
"""N Queens"""

import sys


def print_usage_and_exit():
    """Prints the usage message and exits with status 1."""
    print("Usage: nqueens N")
    sys.exit(1)


def print_number_error_and_exit():
    """Prints an error message indicating that N must be a number
    and exits with status 1."""
    print("N must be a number")
    sys.exit(1)


def print_size_error_and_exit():
    """Prints an error message indicating that N must be at least
    4 and exits with status 1."""
    print("N must be at least 4")
    sys.exit(1)


def is_valid(board, row, col):
    """
    Checks if it's valid to place a queen at board[row][col].

    Args:
        board (list): The current board configuration.
        row (int): The row where the queen is to be placed.
        col (int): The column where the queen is to be placed.

    Returns:
        bool: True if the placement is valid, False otherwise.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n):
    """
    Solves the N-Queens problem and returns a list of solutions.

    Args:
        n (int): The size of the chessboard (N x N).

    Returns:
        list: A list of solutions, where each solution is represented
        as a list of [row, col] pairs.
    """
    def backtrack(row):
        """Recursively places queens and collects valid solutions."""
        if row == n:
            solutions.append(list(enumerate(board)))
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    board = [-1] * n  # Initialize board with -1 (no queens placed)
    solutions = []    # List to store solutions
    backtrack(0)
    return solutions


def main():
    """Main function to handle user input, solve the problem,
    and print solutions."""
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        n = int(sys.argv[1])
    except ValueError:
        print_number_error_and_exit()

    if n < 4:
        print_size_error_and_exit()

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
