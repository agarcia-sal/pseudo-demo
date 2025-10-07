def string_xor(a: str, b: str) -> str:
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'
    zipped_pairs = list(zip(a, b))
    result_characters = []
    for pair in zipped_pairs:
        x = pair[0]
        y = pair[1]
        xor_result = xor(x, y)
        result_characters.append(xor_result)
    result_string = ''.join(result_characters)
    return result_string