from typing import Callable

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_i: str, character_j: str) -> str:
        return '1' if character_i != character_j else '0'

    output = []
    idx = 0
    len_a, len_b = len(string_a), len(string_b)
    while idx < len_a and idx < len_b:
        output.append(xor(string_a[idx], string_b[idx]))
        idx += 1
    return ''.join(output)