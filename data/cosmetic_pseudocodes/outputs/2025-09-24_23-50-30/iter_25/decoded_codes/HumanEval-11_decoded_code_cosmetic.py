from typing import Callable

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_p: str, character_q: str) -> str:
        # Returns '0' if characters are equal, '1' otherwise
        return '0' if character_p == character_q else '1'

    accumulator: str = ""
    index_n: int = 0

    while index_n < len(string_a) and index_n < len(string_b):
        current_char_1: str = string_a[index_n]
        current_char_2: str = string_b[index_n]
        accumulator += xor(current_char_1, current_char_2)
        index_n += 1

    return accumulator