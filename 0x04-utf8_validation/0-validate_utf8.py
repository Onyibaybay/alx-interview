#!/usr/bin/python3
"""
This module provides a function to validate UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): List of integers where each integer represents a byte
                     (8 bits).

    Returns:
        bool: True if the data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0  # Number of bytes left in the current UTF-8 character

    MASK1 = 1 << 7  # 10000000 in binary
    MASK2 = 1 << 6  # 01000000 in binary

    for byte in data:
        byte = byte & 0xFF  # Only keep the 8 least significant bits

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if byte & MASK1 == 0:
                continue  # 1-byte character (0xxxxxxx)
            elif byte & (MASK1 | MASK2) == MASK1:
                return False  # Invalid continuation byte found
            else:
                # Count the leading 1s to determine byte length
                mask = MASK1
                while byte & mask:
                    num_bytes += 1
                    mask >>= 1

                if num_bytes == 1 or num_bytes > 4:
                    return False  # Invalid UTF-8 length

                num_bytes -= 1  # Account for the current byte
        else:
            # Check if it's a valid continuation byte (10xxxxxx)
            if byte & (MASK1 | MASK2) != MASK2:
                return False
            num_bytes -= 1

    return num_bytes == 0  # Ensure all bytes are used up

