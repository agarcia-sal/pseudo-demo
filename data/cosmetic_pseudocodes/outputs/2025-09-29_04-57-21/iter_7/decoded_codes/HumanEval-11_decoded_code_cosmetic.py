from typing import Callable


def string_xor(string_a: str, string_b: str) -> str:
    def xor(char_m: str, char_n: str) -> str:
        # Returns '0' if chars are equal, else '1'
        return '0' if char_m == char_n else '1'

    output_str = []
    index_pos = 0
    len_a, len_b = len(string_a), len(string_b)
    while index_pos < len_a and index_pos < len_b:
        current_char1 = string_a[index_pos]
        current_char2 = string_b[index_pos]
        output_str.append(xor(current_char1, current_char2))
        index_pos += 1
    return ''.join(output_str)