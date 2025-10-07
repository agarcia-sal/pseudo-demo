def string_xor(string_a: str, string_b: str) -> str:
    def xor(char_m: str, char_n: str) -> str:
        return '1' if char_m != char_n else '0'

    output_str = []
    idx = 0
    while idx < len(string_a) and idx < len(string_b):
        output_str.append(xor(string_a[idx], string_b[idx]))
        idx += 1

    return ''.join(output_str)