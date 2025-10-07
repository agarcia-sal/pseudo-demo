def string_xor(a: str, b: str) -> str:
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'
    result_list = []
    length = len(a)
    for index in range(length):
        x = a[index]
        y = b[index]
        xor_value = xor(x, y)
        result_list.append(xor_value)
    result_string = ''
    for index in range(len(result_list)):
        element = result_list[index]
        result_string += element
    return result_string