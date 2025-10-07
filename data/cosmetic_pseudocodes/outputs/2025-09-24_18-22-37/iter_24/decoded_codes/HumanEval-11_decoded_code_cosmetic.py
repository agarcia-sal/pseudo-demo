from typing import Literal

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_i: str, character_j: str) -> Literal['0', '1']:
        return '1' if character_i != character_j else '0'

    length_p = len(string_a)
    accumulated_result = ''.join(
        xor(string_a[i], string_b[i]) for i in range(length_p)
    )
    return accumulated_result