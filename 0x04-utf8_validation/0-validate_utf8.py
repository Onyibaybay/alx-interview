#!/usr/bin/python3
"""
Determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing bytes.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Masks to check the leading bits of a byte
    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        # Get the 8 least significant bits
        byte = num & 0xFF

        if n_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            mask = 1 << 7
            while mask & byte:
                n_bytes += 1
                mask = mask >> 1

            # 1-byte character (ASCII), continue to next byte
            if n_bytes == 0:
                continue

            # UTF-8 allows 1 to 4 bytes only
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Check that the byte is in the format 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Move to the next byte in the current UTF-8 character
        n_bytes -= 1

    # If n_bytes is not zero, we have an incomplete character
    return n_bytes == 0
