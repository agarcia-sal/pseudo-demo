def string_xor(string_a: str, string_b: str) -> str:
    def xor(char1: str, char2: str) -> str:
        return '0' if char1 == char2 else '1'

    output_string = []
    for c1, c2 in zip(string_a, string_b):
        output_string.append(xor(c1, c2))
    return ''.join(output_string)