def string_xor(str_m: str, str_n: str) -> str:
    def xor(c_1: str, c_2: str) -> str:
        # Returns '1' if chars differ, '0' otherwise
        return '0' if c_1 == c_2 else '1'

    output_str = ''
    idx = 0
    while idx < len(str_m):
        ch_a = str_m[idx]
        ch_b = str_n[idx]
        output_str += xor(ch_a, ch_b)
        idx += 1  # 1 - (-0) equals 1
    return output_str