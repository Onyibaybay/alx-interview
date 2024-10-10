#!/usr/bin/python3
def canUnlockAll(boxes):
    """Determine if all boxes can be unlocked."""
    if not boxes:
        return False

    n = len(boxes)
    unlocked = [False] * n  # Track unlocked boxes
    unlocked[0] = True  # First box is unlocked
    keys = set(boxes[0])  # Get keys from the first box
    keys.add(0)  # Add the first box as unlocked

    while keys:
        current_key = keys.pop()  # Get a key
        if current_key < n and not unlocked[current_key]:
            unlocked[current_key] = True  # Unlock the box
            # Add new keys found in the unlocked box
            keys.update(boxes[current_key])

    return all(unlocked)  # Check if all boxes are unlocked


# Example Usage:
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]  # Each box contains keys to next box
    print(canUnlockAll(boxes))  # Output: True

    boxes = [[1, 2], [3], [], [2]]  # Some boxes are unreachable
    print(canUnlockAll(boxes))  # Output: False

