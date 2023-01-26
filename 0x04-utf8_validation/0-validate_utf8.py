#!/usr/bin/python3
"""Valid UTF8 module
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """Determine if a given data set represents a valid UTF-8 encoding.

    Args:
        data (List[int]): The data set to check, represented by a
            list of integers. Each integer represents 1 byte of data,
            therefore you only need to handle the 8 least significant bits of each integer.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False
    """
    bytes_to_check = 0

    for byte in data:
        # Get the 8 least significant bits from thte current byte
        byte = byte & 0b11111111

        # If this is the start of a new character
        if bytes_to_check == 0:
            # A single byte character
            if (byte >> 7) == 0:
                continue
            # A multiple-byte character
            elif (byte >> 5) == 0b110:
                bytes_to_check = 1
            elif (byte >> 4) == 0b1110:
                bytes_to_check = 2
            elif (byte >> 3) == 0b11110:
                bytes_to_check = 3
            else:
                return False
        else:
            # The following bytes should have the form 10xxxxxx
            if (byte >> 6) != 0b10:
                return False
            bytes_to_check -= 1

    # If all bytes have been checked and there's no bytes left to check, then it's valid UTF-8
    return bytes_to_check == 0
