from typing import Literal

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_p: str, character_q: str) -> Literal['0', '1']:
        if character_p == character_q:
            return '0'
        else:
            return '1'

    accumulator = []
    index_counter = 0
    length_a = len(string_a)
    length_b = len(string_b)
    while index_counter < length_a and index_counter < length_b:
        temp_char_m = string_a[index_counter]
        temp_char_n = string_b[index_counter]
        intermediate_result = xor(temp_char_m, temp_char_n)
        accumulator.append(intermediate_result)
        index_counter += 1

    return ''.join(accumulator)