from typing import List

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_e: str, character_f: str) -> str:
        if character_e == character_f:
            return '0'
        return '1'

    result_array: List[str] = []
    index_g = 0
    while index_g < len(string_a) and index_g < len(string_b):
        result_array.append(xor(string_a[index_g], string_b[index_g]))
        index_g += 1

    result_string = ''.join(result_array)
    return result_string