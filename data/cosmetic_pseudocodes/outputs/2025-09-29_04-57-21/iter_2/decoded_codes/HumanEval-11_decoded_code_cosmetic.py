def string_xor(string_a: str, string_b: str) -> str:
    def xor(char_m: str, char_n: str) -> str:
        return '1' if char_m != char_n else '0'

    return ''.join(xor(string_a[i], string_b[i]) for i in range(len(string_a)))