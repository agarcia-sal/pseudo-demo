from typing import Tuple

def reverse_delete(str_x: str, str_y: str) -> Tuple[str, bool]:
    str_z: str = ""
    idx_a: int = 0
    while idx_a < len(str_x):
        ch_b: str = str_x[idx_a]
        if ch_b not in str_y:
            str_z += ch_b
        idx_a += 1

    rev_str: str = ""
    idx_c: int = len(str_z) - 1
    while idx_c >= 0:
        rev_str += str_z[idx_c]
        idx_c -= 1

    is_pal: bool = False
    if rev_str == str_z:
        is_pal = True

    return str_z, is_pal