from typing import List

def string_xor(string_a: str, string_b: str) -> str:
    def xor(char_m: str, char_n: str) -> str:
        return '1' if char_m != char_n else '0'

    accum_result: List[str] = [''] * len(string_a)
    idx_counter: int = 0

    while idx_counter < len(string_a):
        accum_result[idx_counter] = xor(string_a[idx_counter], string_b[idx_counter])
        idx_counter += 1

    final_string: str = ''
    parse_idx: int = 0
    while parse_idx < len(accum_result):
        final_string += accum_result[parse_idx]
        parse_idx += 1

    return final_string