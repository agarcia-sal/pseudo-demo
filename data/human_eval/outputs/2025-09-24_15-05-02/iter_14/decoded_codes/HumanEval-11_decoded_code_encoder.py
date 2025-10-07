def string_xor(a, b):
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    result = ''
    for x, y in zip(a, b):
        result += xor(x, y)
    return result