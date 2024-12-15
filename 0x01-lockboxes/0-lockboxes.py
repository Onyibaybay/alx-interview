#!/usr/bin/python3
"""
Lockboxes Problem

This script contains a method to determine if all the boxes in a
given list of lists can be unlocked.
Each box is numbered sequentially from 0 to n - 1 and may contain
keys to other boxes. The goal is to check if all boxes can be opened
starting from the first box, which is initially unlocked.

"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Parameters:
    boxes (list of lists): List where each element is a list of
    keys contained in that box.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    return all(unlocked)
