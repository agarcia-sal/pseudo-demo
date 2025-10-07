from typing import Callable


def string_xor(string_a: str, string_b: str) -> str:
    def xor(char1: str, char2: str) -> str:
        return '0' if char1 == char2 else '1'

    return ''.join(xor(c1, c2) for c1, c2 in zip(string_a, string_b))