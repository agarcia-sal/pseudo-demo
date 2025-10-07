def string_xor(string_a: str, string_b: str) -> str:
    def xor(bit_i: str, bit_j: str) -> str:
        if bit_i == bit_j:
            return '0'
        else:
            return '1'

    result_string = []
    for bit_a, bit_b in zip(string_a, string_b):
        result_string.append(xor(bit_a, bit_b))
    return ''.join(result_string)