from typing import Callable


def string_xor(string_a: str, string_b: str) -> str:
    def xor(char_alpha: str, char_beta: str) -> str:
        return '0' if char_alpha == char_beta else '1'

    accumulator = []
    index_counter = 0
    len_a = len(string_a)
    len_b = len(string_b)
    while index_counter < len_a and index_counter < len_b:
        element_1 = string_a[index_counter]
        element_2 = string_b[index_counter]
        accumulator.append(xor(element_1, element_2))
        index_counter += 1

    return ''.join(accumulator)