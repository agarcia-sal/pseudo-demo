def string_xor(a: str, b: str) -> str:
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'
    result = []
    index = 0
    while index < len(a):
        x = a[index]
        y = b[index]
        temp = xor(x, y)
        result.append(temp)
        index += 1
    output = ''
    index = 0
    while index < len(result):
        output += result[index]
        index += 1
    return output