from typing import Callable

def string_xor(str1: str, str2: str) -> str:
    def xor(char_m: str, char_n: str) -> str:
        if char_m == char_n:
            return '0'
        return '1'

    output_str = []
    index_var = 0
    len1, len2 = len(str1), len(str2)
    while index_var < len1 and index_var < len2:
        a_char = str1[index_var]
        b_char = str2[index_var]
        temp = xor(a_char, b_char)
        output_str.append(temp)
        index_var += 1

    return ''.join(output_str)