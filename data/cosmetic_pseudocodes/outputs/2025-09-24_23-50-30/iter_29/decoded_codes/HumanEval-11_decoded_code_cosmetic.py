def string_xor(str_m: str, str_n: str) -> str:
    def xor(char_p: str, char_q: str) -> str:
        return '0' if char_p == char_q else '1'

    return ''.join(xor(str_m[i], str_n[i]) for i in range(len(str_m)))