from typing import Iterator, Tuple


def string_xor(string_a: str, string_b: str) -> str:
    def xor(char_i: str, char_j: str) -> str:
        return '0' if char_i == char_j else '1'

    result_chars = [xor(x, y) for x, y in zip(string_a, string_b)]
    return ''.join(result_chars)