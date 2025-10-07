def string_xor(a: str, b: str) -> str:
    def xor(i: str, j: str) -> str:
        if i == j:
            return '0'
        else:
            return '1'
    result = []
    length = len(a)
    index = 0
    while index < length:
        x = a[index]
        y = b[index]
        call_result = xor(x, y)
        result.append(call_result)
        index += 1
    joined_result = ''
    join_index = 0
    result_length = len(result)
    while join_index < result_length:
        joined_result += result[join_index]
        join_index += 1
    return joined_result