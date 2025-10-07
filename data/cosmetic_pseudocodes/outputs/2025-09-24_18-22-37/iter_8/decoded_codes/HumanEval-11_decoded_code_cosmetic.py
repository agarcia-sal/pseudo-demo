from typing import Callable

def string_xor(input_str1: str, input_str2: str) -> str:
    def xor(char_one: str, char_two: str) -> str:
        return '0' if char_one == char_two else '1'

    accumulator: str = ""
    iter_index: int = 0
    length_limit: int = len(input_str1)

    while iter_index < length_limit:
        element_a: str = input_str1[iter_index]
        element_b: str = input_str2[iter_index]
        temp_result: str = xor(element_a, element_b)
        accumulator += temp_result
        iter_index += 1

    return accumulator