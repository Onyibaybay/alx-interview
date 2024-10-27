#!/usr/bin/python3
""" Minimum Opoerations """


def minOperations(n):
    """
    Calculates the minimum number of operations needed to get
    exactly n 'H' characters in the file using only 'Copy All'
    and 'Paste' operations.

    Parameters:
    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations required.
    If n is impossible to achieve, return 0.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while factor <= n:
        while n % factor == 0:
            operations += factor
            n = n // factor
        factor += 1

    return operations