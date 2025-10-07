def string_xor(a: str, b: str) -> str:
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'
    result = ""
    index = 0
    while index < len(a):
        x = a[index]
        y = b[index]
        char = xor(x, y)
        result += char
        index += 1
    return result