from __future__ import annotations


def encode_shift(string_input: str) -> str:
    return ''.join(
        chr(((ord(ch) + 5 - ord('a')) % 26) + ord('a'))
        for ch in string_input
    )


def decode_shift(string_input: str) -> str:
    return ''.join(
        chr(((ord(ch) - 5 - ord('a')) % 26) + ord('a'))
        for ch in string_input
    )