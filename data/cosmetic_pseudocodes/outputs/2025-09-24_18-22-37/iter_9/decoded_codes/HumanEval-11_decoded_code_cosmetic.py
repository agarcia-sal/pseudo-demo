from typing import Callable

def string_xor(string_a: str, string_b: str) -> str:
    def xor(char_m: str, char_n: str) -> str:
        if char_m == char_n:
            return '0'
        return '1'

    accumulated_result = []
    iterator_index = 0
    length = min(len(string_a), len(string_b))
    while iterator_index < length:
        left_char = string_a[iterator_index]
        right_char = string_b[iterator_index]
        xor_output = xor(left_char, right_char)
        accumulated_result.append(xor_output)
        iterator_index += 1

    return ''.join(accumulated_result)