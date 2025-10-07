def string_xor(a: str, b: str) -> str:
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'
    result = ''
    length = 0
    while length < len(a) and length < len(b):
        x = a[length]
        y = b[length]
        temp = xor(x, y)
        result += temp
        length += 1
    return result