def string_xor(a: str, b: str) -> str:
    def xor(i: str, j: str) -> str:
        return '0' if i == j else '1'
    length = min(len(a), len(b))
    result = [xor(a[i], b[i]) for i in range(length)]
    return ''.join(result)