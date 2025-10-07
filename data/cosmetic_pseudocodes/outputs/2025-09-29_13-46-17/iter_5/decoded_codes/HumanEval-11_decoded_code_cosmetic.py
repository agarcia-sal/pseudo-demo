from typing import Literal

def string_xor(string_a: str, string_b: str) -> str:
    def xor(char_one: str, char_two: str) -> Literal['0', '1']:
        return '0' if char_one == char_two else '1'

    idx_counter = 0
    acc_string = ""
    while idx_counter < len(string_a) and idx_counter < len(string_b):
        acc_string += xor(string_a[idx_counter], string_b[idx_counter])
        idx_counter += 1

    return acc_string