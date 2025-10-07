from typing import List

def encode_shift(input_string: str) -> str:
    base = ord('a')
    return ''.join(
        chr((ord(c) + 5 - base) % 26 + base) if 'a' <= c <= 'z' else c
        for c in input_string
    )

def decode_shift(input_string: str) -> str:
    base = ord('a')
    return ''.join(
        chr((ord(c) - 5 - base) % 26 + base) if 'a' <= c <= 'z' else c
        for c in input_string
    )