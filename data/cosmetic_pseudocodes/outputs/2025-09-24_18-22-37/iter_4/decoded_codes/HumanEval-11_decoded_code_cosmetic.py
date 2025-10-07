def string_xor(input_str1: str, input_str2: str) -> str:
    def xor_func(char1: str, char2: str) -> str:
        return '0' if char1 == char2 else '1'

    output_str = []
    index = 0
    length1 = len(input_str1)
    length2 = len(input_str2)
    while index < length1 and index < length2:
        output_str.append(xor_func(input_str1[index], input_str2[index]))
        index += 1
    return ''.join(output_str)