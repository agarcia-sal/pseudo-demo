from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, str]:
    list_y: list[str] = []
    index_z: int = 0
    while index_z < len(string_s):
        char_p: str = string_s[index_z]
        if char_p not in string_c:
            list_y = list_y + [char_p]
        index_z += 1
    str_q: str = ""
    idx_r: int = 0
    while idx_r < len(list_y):
        str_q += list_y[idx_r]
        idx_r += 1
    rev_s: str = ""
    idx_t: int = len(str_q) - 1
    while idx_t >= 0:
        rev_s += str_q[idx_t]
        idx_t -= 1
    return (str_q, rev_s)