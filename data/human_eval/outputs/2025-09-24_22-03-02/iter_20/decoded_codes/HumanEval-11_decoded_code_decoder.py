def string_xor(a: str, b: str) -> str:
    def xor(i: str, j: str) -> str:
        return '0' if i == j else '1'

    result = []
    length = len(a)
    index = 0
    while index < length:
        x = a[index]
        y = b[index]
        char = xor(x, y)
        result.append(char)
        index += 1

    return ''.join(result)