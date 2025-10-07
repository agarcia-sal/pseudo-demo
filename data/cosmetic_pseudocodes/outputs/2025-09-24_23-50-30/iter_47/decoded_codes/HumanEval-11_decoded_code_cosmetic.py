from typing import Callable

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_u: str, character_v: str) -> str:
        if character_u != character_v:
            return '1'
        return '0'

    output_string = ''
    index_counter = 0
    while index_counter < len(string_a) and index_counter < len(string_b):
        current_char_1 = string_a[index_counter]
        current_char_2 = string_b[index_counter]
        output_string += xor(current_char_1, current_char_2)
        index_counter += 1
    return output_string