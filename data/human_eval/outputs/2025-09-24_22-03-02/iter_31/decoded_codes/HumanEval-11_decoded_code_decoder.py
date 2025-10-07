def string_xor(a: str, b: str) -> str:
    def xor(i, j):
        return '0' if i == j else '1'
    result = []
    length = len(a)
    index = 0
    while index < length:
        x = a[index:index + 1]
        y = b[index:index + 1]
        temp = xor(x, y)
        result.append(temp)
        index += 1
    joined_result = ''
    index = 0
    result_length = len(result)
    while index < result_length:
        joined_result += result[index]
        index += 1
    return joined_result