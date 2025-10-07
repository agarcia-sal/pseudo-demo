from typing import Iterator

def string_xor(string_a: str, string_b: str) -> str:
    def xor(bit_i: str, bit_j: str) -> str:
        if bit_i == bit_j:
            return '0'
        else:
            return '1'

    # zip stops at the shortest input length; that matches the original pseudocode behavior
    return ''.join(xor(x, y) for x, y in zip(string_a, string_b))