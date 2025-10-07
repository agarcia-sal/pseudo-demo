from typing import Callable

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_m: str, character_n: str) -> str:
        if character_m == character_n:
            return '0'
        else:
            return '1'

    assembled_result = []
    length_limit = len(string_a)
    for iterator_index in range(length_limit):
        first_char = string_a[iterator_index]
        second_char = string_b[iterator_index]
        temp_char_result = xor(first_char, second_char)
        assembled_result.append(temp_char_result)
    return ''.join(assembled_result)