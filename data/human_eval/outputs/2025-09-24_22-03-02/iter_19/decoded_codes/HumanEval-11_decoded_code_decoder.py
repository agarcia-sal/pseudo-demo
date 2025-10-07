def string_xor(a: str, b: str) -> str:
    def xor(i: str, j: str) -> str:
        if i == j:
            return '0'
        else:
            return '1'
    result = []
    min_length = len(a)
    if len(b) < len(a):
        min_length = len(b)
    index = 0
    while index < min_length:
        x = a[index]
        y = b[index]
        xor_result = xor(x, y)
        result.append(xor_result)
        index += 1
    joined_result = ""
    index = 0
    while index < len(result):
        joined_result += result[index]
        index += 1
    return joined_result