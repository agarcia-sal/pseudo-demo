from typing import Literal

def string_xor(string_m: str, string_n: str) -> str:
    def xor(c_alpha: str, c_beta: str) -> Literal['0', '1']:
        return '1' if c_alpha != c_beta else '0'

    acc = []
    idx = 0

    while idx < len(string_m) and idx < len(string_n):
        acc.append(xor(string_m[idx], string_n[idx]))
        idx += 1

    return "".join(acc)