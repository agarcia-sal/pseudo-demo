from typing import List

def string_xor(string_a: str, string_b: str) -> str:
    def xor(bit_i: str, bit_j: str) -> str:
        if bit_i == bit_j:
            return '0'
        else:
            return '1'

    result_bits: List[str] = []
    for bit_x, bit_y in zip(string_a, string_b):
        xor_bit = xor(bit_x, bit_y)
        result_bits.append(xor_bit)
    result_string = ''.join(result_bits)
    return result_string