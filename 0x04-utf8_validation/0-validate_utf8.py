#!/usr/bin/python3
"""UTF8 Validation."""


def validUTF8(data):
    """
    Method that determines if a given data set represents a valid
    UTF-8 encoding.
    Return: True if data is a valid UTF-8 encoding, else return False
    """

    # Variable for tracking the number of bytes in UTF-8 Character
    byte_count = 0

    # Masks for checking if byte is a continuation byte (Starts with 10)
    mask_high = 1 << 7
    mask_low = 1 << 6

    for byte in data:

        current_mask = 1 << 7

        if byte_count == 0:
            # Determine the number of bytes in the UTF-8 character
            while current_mask & byte:
                byte_count += 1
                current_mask >>= 1

            # If byte count did not increase, it means it's a 1-byte character
            # No need to check the next bytes for this character
            if byte_count == 0:
                continue

            # UTF-8 characters can be 1 to 4 bytes long
            # 1-byte characters start with 0, so byte_count should never be 1
            if byte_count == 1 or byte_count > 4:
                return False

        else:
            # Every byte that is not the first byte of a character should start
            # with 10, otherwise it is not valid
            if not (byte & mask_high and not (byte & mask_low)):
                return False

        # If the bytes for the character are valid, decrease the count
        byte_count -= 1

    # All characters were verified correctly with their proper byte count
    return byte_count == 0
