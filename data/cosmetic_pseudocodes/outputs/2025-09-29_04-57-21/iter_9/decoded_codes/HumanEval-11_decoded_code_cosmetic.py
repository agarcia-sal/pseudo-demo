from typing import Callable

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_i: str, character_j: str) -> str:
        return '0' if not (character_i != character_j) else '1'

    combined_result = []
    index_counter = 0
    length_a = len(string_a)
    length_b = len(string_b)
    while index_counter < length_a and index_counter < length_b:
        current_char1 = string_a[index_counter]
        current_char2 = string_b[index_counter]
        combined_result.append(xor(current_char1, current_char2))
        index_counter += 1
    return ''.join(combined_result)