from typing import Literal


def string_xor(string_a: str, string_b: str) -> str:
    def xor(char_m: str, char_n: str) -> Literal['0', '1']:
        if char_m == char_n:
            return '0'
        return '1'

    accumulator: str = ""
    index_counter: int = 0
    while index_counter < len(string_a) and index_counter < len(string_b):
        element_m = string_a[index_counter]
        element_n = string_b[index_counter]
        accumulator += xor(element_m, element_n)
        index_counter += 1
    return accumulator