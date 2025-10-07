from typing import Literal

def string_xor(string_a: str, string_b: str) -> str:
    def xor(char_m: str, char_n: str) -> Literal['0', '1']:
        return '1' if char_m != char_n else '0'

    aggregate_result = []
    idx = 0
    len_a = len(string_a)
    len_b = len(string_b)
    while idx < len_a and idx < len_b:
        aggregate_result.append(xor(string_a[idx], string_b[idx]))
        idx += 1
    return ''.join(aggregate_result)