from typing import Literal


def string_xor(string_a: str, string_b: str) -> str:
    def xor(char_m: str, char_n: str) -> Literal['0', '1']:
        if char_m == char_n:
            return '0'
        return '1'

    accumulator = []
    for index in range(len(string_a)):
        accumulator.append(xor(string_a[index], string_b[index]))
    return ''.join(accumulator)