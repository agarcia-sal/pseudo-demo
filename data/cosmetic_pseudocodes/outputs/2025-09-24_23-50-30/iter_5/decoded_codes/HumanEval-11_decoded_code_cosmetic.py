from typing import Callable

def string_xor(string_a: str, string_b: str) -> str:
    def xor(char_p: str, char_q: str) -> str:
        if char_p == char_q:
            return '0'
        return '1'

    accumulator = []
    index_counter = 0

    while index_counter < len(string_a) and index_counter < len(string_b):
        elem_p = string_a[index_counter]
        elem_q = string_b[index_counter]
        res_char = xor(elem_p, elem_q)
        accumulator.append(res_char)
        index_counter += 1

    return ''.join(accumulator)