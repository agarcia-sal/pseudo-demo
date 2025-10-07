def string_xor(a: str, b: str) -> str:
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    result = ''
    length = min(len(a), len(b))
    for index in range(length):
        x = a[index]
        y = b[index]
        temp = xor(x, y)
        result += temp
    return result