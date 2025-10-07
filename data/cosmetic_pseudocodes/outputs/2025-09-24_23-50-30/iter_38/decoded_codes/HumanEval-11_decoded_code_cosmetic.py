def string_xor(string_m: str, string_n: str) -> str:
    def xor(char_p: str, char_q: str) -> str:
        return '0' if char_p == char_q else '1'

    output_str = ''
    index_pos = 0

    while index_pos < len(string_m):
        char_a = string_m[index_pos]
        char_b = string_n[index_pos]
        output_str += xor(char_a, char_b)
        index_pos += 1

    return output_str