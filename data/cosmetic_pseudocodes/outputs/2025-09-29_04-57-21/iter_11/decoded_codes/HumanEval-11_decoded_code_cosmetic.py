def string_xor(string_p: str, string_q: str) -> str:
    def xor(char_m: str, char_n: str) -> str:
        return '1' if char_m != char_n else '0'

    return ''.join(xor(string_p[i], string_q[i]) for i in range(len(string_p)))