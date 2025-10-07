from typing import Callable

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_i: str, character_j: str) -> str:
        return '0' if character_i == character_j else '1'

    length = min(len(string_a), len(string_b))
    return ''.join(xor(string_a[i], string_b[i]) for i in range(length))