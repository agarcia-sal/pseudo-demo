from typing import Callable

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_i: str, character_j: str) -> str:
        return '0' if character_i == character_j else '1'

    return ''.join(xor(c_x, c_y) for c_x, c_y in zip(string_a, string_b))