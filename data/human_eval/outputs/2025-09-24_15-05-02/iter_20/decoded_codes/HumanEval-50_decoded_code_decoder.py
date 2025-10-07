from typing import Iterable

def encode_shift(string_s: str) -> str:
    return ''.join(
        chr(((ord(ch) + 5 - ord('a')) % 26) + ord('a'))
        for ch in string_s
    )

def decode_shift(string_s: str) -> str:
    return ''.join(
        chr(((ord(ch) - 5 - ord('a')) % 26) + ord('a'))
        for ch in string_s
    )