from typing import Generator

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_i: str, character_j: str) -> str:
        return '0' if character_i == character_j else '1'

    return ''.join(xor(x, y) for x, y in zip(string_a, string_b))