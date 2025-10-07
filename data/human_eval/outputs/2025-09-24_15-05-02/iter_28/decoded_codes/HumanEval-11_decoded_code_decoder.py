from typing import Iterator

def string_xor(string_a: str, string_b: str) -> str:
    def xor(bit_i: str, bit_j: str) -> str:
        return '0' if bit_i == bit_j else '1'

    return ''.join(xor(x, y) for x, y in zip(string_a, string_b))