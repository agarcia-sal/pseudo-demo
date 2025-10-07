def string_xor(string_a, string_b):
    def xor(bit_i, bit_j):
        if bit_i == bit_j:
            return '0'
        else:
            return '1'

    result_string = ''
    for x, y in zip(string_a, string_b):
        result_string += xor(x, y)
    return result_string