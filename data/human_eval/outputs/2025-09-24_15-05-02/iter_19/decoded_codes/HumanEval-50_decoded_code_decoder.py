from typing import Optional

def encode_shift(string_input: str) -> str:
    return ''.join(
        chr((ord(character) + 5 - ord('a')) % 26 + ord('a'))
        for character in string_input
    )

def decode_shift(string_input: str) -> str:
    return ''.join(
        chr((ord(character) - 5 - ord('a')) % 26 + ord('a'))
        for character in string_input
    )