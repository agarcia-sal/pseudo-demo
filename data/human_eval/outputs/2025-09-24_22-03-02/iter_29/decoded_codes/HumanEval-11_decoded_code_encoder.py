def string_xor(a: str, b: str) -> str:
    def xor(i: str, j: str) -> str:
        return '0' if i == j else '1'
    result = []
    index = 0
    length = min(len(a), len(b))
    while index < length:
        x = a[index]
        y = b[index]
        value = xor(x, y)
        result.append(value)
        index += 1
    joined_result = ''.join(result)
    return joined_result