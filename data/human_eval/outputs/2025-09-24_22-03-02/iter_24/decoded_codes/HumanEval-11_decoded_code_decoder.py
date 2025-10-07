def string_xor(a: str, b: str) -> str:
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'
    result = []
    index = 0
    while index < len(a) and index < len(b):
        x = a[index]
        y = b[index]
        result.append(xor(x, y))
        index += 1
    joined_result = ''
    result_index = 0
    while result_index < len(result):
        joined_result += result[result_index]
        result_index += 1
    return joined_result