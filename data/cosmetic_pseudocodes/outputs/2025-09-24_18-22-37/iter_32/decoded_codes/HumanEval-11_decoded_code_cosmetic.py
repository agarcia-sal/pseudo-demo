from typing import Callable


def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_p: str, character_q: str) -> str:
        return '1' if character_p != character_q else '0'

    accumulation_string = ""
    position_index = 0
    length_limit = len(string_a)

    while position_index < length_limit:
        element_m = string_a[position_index]
        element_n = string_b[position_index]
        accumulation_string += xor(element_m, element_n)
        position_index += 1

    return accumulation_string