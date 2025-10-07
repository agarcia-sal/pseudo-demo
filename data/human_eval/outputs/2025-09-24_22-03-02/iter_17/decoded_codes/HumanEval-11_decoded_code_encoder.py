def string_xor(a: str, b: str) -> str:
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'
    result = []
    zipped = list(zip(a, b))
    for pair in zipped:
        x = pair[0]
        y = pair[1]
        value = xor(x, y)
        result.append(value)
    output = ''.join(result)
    return output