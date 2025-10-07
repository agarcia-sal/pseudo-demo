from typing import Iterator

def string_xor(string_a: str, string_b: str) -> str:
    def xor(char_i: str, char_j: str) -> str:
        if char_i == char_j:
            return '0'
        else:
            return '1'

    if len(string_a) != len(string_b):
        raise ValueError("Input strings must be of the same length")

    return ''.join(xor(x, y) for x, y in zip(string_a, string_b))