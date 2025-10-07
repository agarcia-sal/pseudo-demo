from typing import Callable

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_p: str, character_q: str) -> str:
        return '1' if character_p != character_q else '0'

    accumulation_result = []
    length_n = len(string_a)
    for index_m in range(length_n):
        char_alpha = string_a[index_m]
        char_beta = string_b[index_m]
        temp_z = xor(char_alpha, char_beta)
        accumulation_result.append(temp_z)
    return ''.join(accumulation_result)