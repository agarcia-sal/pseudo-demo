from typing import Callable

def string_xor(string_p: str, string_q: str) -> str:
    def xor(char_m: str, char_n: str) -> str:
        if char_m == char_n:
            return '0'
        else:
            return '1'

    accumulated_result = []
    index_counter = 0
    len_p = len(string_p)
    len_q = len(string_q)

    while index_counter < len_p and index_counter < len_q:
        elem_a = string_p[index_counter]
        elem_b = string_q[index_counter]
        accumulated_result.append(xor(elem_a, elem_b))
        index_counter += 1

    return ''.join(accumulated_result)