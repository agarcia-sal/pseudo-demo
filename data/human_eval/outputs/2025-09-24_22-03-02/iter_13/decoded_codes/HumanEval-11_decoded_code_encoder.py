def string_xor(a: str, b: str) -> str:
    def xor(i: str, j: str) -> str:
        if i == j:
            return '0'
        else:
            return '1'
    result = []
    for x, y in zip(a, b):
        result.append(xor(x, y))
    final_result = ''.join(result)
    return final_result