from typing import Literal

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_i: str, character_j: str) -> Literal['0', '1']:
        return '0' if character_i == character_j else '1'

    accumulator = []
    index = 0
    len_a = len(string_a)
    len_b = len(string_b)
    while index < len_a and index < len_b:
        accumulator.append(xor(string_a[index], string_b[index]))
        index += 1
    return ''.join(accumulator)