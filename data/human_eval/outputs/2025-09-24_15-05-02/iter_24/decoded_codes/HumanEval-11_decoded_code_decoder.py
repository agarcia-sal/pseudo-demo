from typing import Callable

def string_xor(a_string: str, b_string: str) -> str:
    def xor(bit_i: str, bit_j: str) -> str:
        return '0' if bit_i == bit_j else '1'
    return ''.join(xor(x, y) for x, y in zip(a_string, b_string))