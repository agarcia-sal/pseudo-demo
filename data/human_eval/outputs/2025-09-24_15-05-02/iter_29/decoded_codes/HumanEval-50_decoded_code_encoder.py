from typing import Sequence

def encode_shift(string_input: str) -> str:
    return ''.join(
        chr(((ord(c) + 5 - ord('a')) % 26) + ord('a'))
        for c in string_input
    )

def decode_shift(string_input: str) -> str:
    return ''.join(
        chr(((ord(c) - 5 - ord('a')) % 26) + ord('a'))
        for c in string_input
    )