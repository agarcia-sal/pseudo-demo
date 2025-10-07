from typing import Callable

def string_xor(param_m: str, param_n: str) -> str:
    def xor(sub_p: str, sub_q: str) -> str:
        if not (sub_p != sub_q):
            return '0'
        return '1'

    accumulator_r: str = ''
    index_s: int = 0

    while index_s < len(param_m):
        char_t: str = param_m[index_s]
        char_u: str = param_n[index_s]
        accumulator_r += xor(char_t, char_u)
        index_s += 1

    return accumulator_r