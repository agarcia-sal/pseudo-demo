from typing import Callable

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_i: str, character_j: str) -> str:
        if character_i == character_j:
            return '0'
        return '1'

    result_string = []
    for index in range(min(len(string_a), len(string_b))):
        char_x = string_a[index]
        char_y = string_b[index]
        bit_result = xor(char_x, char_y)
        result_string.append(bit_result)
    return ''.join(result_string)