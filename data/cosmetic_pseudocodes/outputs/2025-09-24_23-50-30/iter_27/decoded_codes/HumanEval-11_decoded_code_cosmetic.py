from typing import List

def string_xor(str_p: str, str_q: str) -> str:
    def xor(char_m: str, char_n: str) -> str:
        if char_m == char_n:
            return '0'
        else:
            return '1'

    res: List[str] = []
    idx = 0
    while idx < len(str_p) and idx < len(str_q):
        elem = xor(str_p[idx], str_q[idx])
        res.append(elem)
        idx += 1
    return ''.join(res)