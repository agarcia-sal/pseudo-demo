from typing import Callable

def string_xor(string_a: str, string_b: str) -> str:
    def xor(bit_i: str, bit_j: str) -> str:
        return '0' if bit_i == bit_j else '1'

    if len(string_a) != len(string_b):
        raise ValueError("Input strings must have the same length")

    result_string = ''.join(xor(string_a[i], string_b[i]) for i in range(len(string_a)))
    return result_string