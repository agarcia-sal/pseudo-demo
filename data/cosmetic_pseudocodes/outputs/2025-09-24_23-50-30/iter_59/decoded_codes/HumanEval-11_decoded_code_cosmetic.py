from typing import Literal

def string_xor(string_p: str, string_q: str) -> str:
    def xor(m: Literal['0', '1'], n: Literal['0', '1']) -> str:
        if m != n:
            return '1'
        return '0'

    result_r = []
    length_t = len(string_p)

    for index_s in range(length_t):
        result_r.append(xor(string_p[index_s], string_q[index_s]))

    return ''.join(result_r)