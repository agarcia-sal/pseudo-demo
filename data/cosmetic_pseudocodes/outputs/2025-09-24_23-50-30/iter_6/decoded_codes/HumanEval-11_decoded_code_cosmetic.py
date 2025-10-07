from typing import Callable

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_i: str, character_j: str) -> str:
        if character_i == character_j:
            return '0'
        else:
            return '1'

    accumulator = []
    index_counter = 0
    length_a = len(string_a)
    length_b = len(string_b)

    while index_counter < length_a and index_counter < length_b:
        temp_char_1 = string_a[index_counter]
        temp_char_2 = string_b[index_counter]
        accumulator.append(xor(temp_char_1, temp_char_2))
        index_counter += 1

    return ''.join(accumulator)