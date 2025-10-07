def string_xor(a: str, b: str) -> str:
    def xor(i: str, j: str) -> str:
        return '0' if i == j else '1'

    result = []
    for x, y in zip(a, b):
        result.append(xor(x, y))
    return ''.join(result)