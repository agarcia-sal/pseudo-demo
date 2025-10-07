from typing import Callable


def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_m: str, character_n: str) -> str:
        if not (character_m != character_n):
            return '0'
        return '1'

    combined_result = []
    iterator_p = 0
    length_a = len(string_a)
    length_b = len(string_b)
    while iterator_p < length_a and iterator_p < length_b:
        char1 = string_a[iterator_p]
        char2 = string_b[iterator_p]
        combined_result.append(xor(char1, char2))
        iterator_p += 1
    return ''.join(combined_result)