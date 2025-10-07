def string_xor(a, b):
    return ''.join('0' if x == y else '1' for x, y in zip(a, b))