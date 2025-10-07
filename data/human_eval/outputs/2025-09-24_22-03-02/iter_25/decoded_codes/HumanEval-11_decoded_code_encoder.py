def string_xor(a: str, b: str) -> str:
    def xor(i, j):
        return '0' if i == j else '1'
    length = min(len(a), len(b))
    result_string = ''.join(xor(a[i], b[i]) for i in range(length))
    return result_string