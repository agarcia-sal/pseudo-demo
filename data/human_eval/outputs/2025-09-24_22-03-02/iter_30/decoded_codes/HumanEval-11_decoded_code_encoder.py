def string_xor(a: str, b: str) -> str:
    def xor(i: str, j: str) -> str:
        return '0' if i == j else '1'
    result = []
    length = len(a)
    index = 0
    while index < length:
        x = a[index]
        y = b[index]
        xor_result = xor(x, y)
        result.append(xor_result)
        index += 1
    output_string = ''.join(result)
    return output_string