def string_xor(a: str, b: str) -> str:
    def xor(i: str, j: str) -> str:
        return '0' if i == j else '1'
    result = ''
    length_a = len(a)
    length_b = len(b)
    min_length = length_a if length_a <= length_b else length_b
    for index in range(min_length):
        char_a = a[index]
        char_b = b[index]
        xor_result = xor(char_a, char_b)
        result += xor_result
    return result