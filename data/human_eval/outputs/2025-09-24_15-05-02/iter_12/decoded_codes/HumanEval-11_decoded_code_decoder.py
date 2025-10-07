def string_xor(string_a: str, string_b: str) -> str:
    def xor(bit_i: str, bit_j: str) -> str:
        return '0' if bit_i == bit_j else '1'

    result_string = []
    for bit_x, bit_y in zip(string_a, string_b):
        result_string.append(xor(bit_x, bit_y))
    return ''.join(result_string)