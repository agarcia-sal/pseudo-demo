from typing import Iterator

def string_xor(string_a: str, string_b: str) -> str:
    def xor(char_i: str, char_j: str) -> str:
        return '0' if char_i == char_j else '1'
    return ''.join(xor(x, y) for x, y in zip(string_a, string_b))