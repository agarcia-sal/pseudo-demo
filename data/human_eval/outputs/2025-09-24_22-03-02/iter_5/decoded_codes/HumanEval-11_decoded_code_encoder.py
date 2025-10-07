def string_xor(a: str, b: str) -> str:
    def xor(i, j):
        return '0' if i == j else '1'
    result = ''
    for x, y in zip(a, b):
        result += xor(x, y)
    return result