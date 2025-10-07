from typing import Callable

def encode_shift(s: str) -> str:
    return ''.join(
        chr(((ord(char) + 5 - ord('a')) % 26) + ord('a'))
        for char in s
    )

def decode_shift(s: str) -> str:
    return ''.join(
        chr(((ord(char) - 5 - ord('a')) % 26) + ord('a'))
        for char in s
    )