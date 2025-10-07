from typing import Callable


def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_i: str, character_j: str) -> str:
        return '0' if character_i == character_j else '1'

    accumulator_string = ''
    index_counter = 0
    while index_counter < len(string_a):
        char_m = string_a[index_counter]
        char_n = string_b[index_counter]
        temp_char = xor(char_m, char_n)
        accumulator_string += temp_char
        index_counter += 1

    return accumulator_string