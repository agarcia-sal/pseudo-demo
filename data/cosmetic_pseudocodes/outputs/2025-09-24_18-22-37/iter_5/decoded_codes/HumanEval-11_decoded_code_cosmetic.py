from typing import Callable

def string_xor(string_a: str, string_b: str) -> str:
    def xor(char_m: str, char_n: str) -> str:
        # Return '0' if chars are equal, else '1'
        if char_m == char_n:
            return '0'
        return '1'

    output_str = []
    len_limit = len(string_a)
    for idx in range(len_limit):
        output_str.append(xor(string_a[idx], string_b[idx]))

    return ''.join(output_str)