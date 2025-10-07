from typing import List


def encrypt(input_string: str) -> str:
    # Convert each character to its ASCII code, shift by position, wrap by 256, then convert back
    return ''.join(
        chr((ord(char) + i) % 256)
        for i, char in enumerate(input_string)
    )