def string_xor(string_a: str, string_b: str) -> str:
    def xor(char_i: str, char_j: str) -> str:
        return '0' if char_i == char_j else '1'

    result_string = []
    for index in range(min(len(string_a), len(string_b))):
        result_string.append(xor(string_a[index], string_b[index]))
    return ''.join(result_string)