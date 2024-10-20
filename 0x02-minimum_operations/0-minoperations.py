#!/usr/bin/python3
"""Minimum Operations module."""


def minoperations(n):
    """
    Calculate the minimum number of operations to get exactly
    n 'H' characters using 'Copy All' and 'Paste' operations.

    Parameters:
    n (int): Target number of 'H' characters.

    Returns:
    int: Minimum operations required, or 0 if impossible.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations

