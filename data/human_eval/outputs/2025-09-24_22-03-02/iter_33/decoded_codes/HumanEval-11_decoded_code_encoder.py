def string_xor(a: str, b: str) -> str:
    def xor(i: str, j: str) -> str:
        if i == j:
            return '0'
        else:
            return '1'

    result = []
    length_a = len(a)
    length_b = len(b)

    min_length = length_a if length_a < length_b else length_b

    index = 0
    while index < min_length:
        char_x = a[index]
        char_y = b[index]
        xor_result = xor(char_x, char_y)
        result.append(xor_result)
        index += 1

    final_result = ""
    result_length = len(result)
    index = 0
    while index < result_length:
        final_result += result[index]
        index += 1

    return final_result