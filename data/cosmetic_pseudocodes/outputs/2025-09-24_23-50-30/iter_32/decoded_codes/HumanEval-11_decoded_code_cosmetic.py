from typing import Literal

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_m: str, character_n: str) -> Literal['0', '1']:
        return '0' if character_m == character_n else '1'

    temp_res = []
    index_p = 0
    len_a = len(string_a)
    len_b = len(string_b)

    while index_p < len_a and index_p < len_b:
        char_r = string_a[index_p]
        char_s = string_b[index_p]
        temp_res.append(xor(char_r, char_s))
        index_p += 1

    return ''.join(temp_res)