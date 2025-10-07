def string_xor(a: str, b: str) -> str:
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'
    result = []
    length_a = len(a)
    length_b = len(b)
    min_length = length_a if length_a < length_b else length_b
    for index in range(min_length):
        element_a = a[index]
        element_b = b[index]
        xor_result = xor(element_a, element_b)
        result.append(xor_result)
    joined_result = ''
    for each_character in range(len(result)):
        joined_result += result[each_character]
    return joined_result