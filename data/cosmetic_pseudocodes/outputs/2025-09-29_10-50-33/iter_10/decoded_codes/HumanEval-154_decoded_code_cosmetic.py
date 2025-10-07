from typing import Literal


def cycpattern_check(string_a: str, string_b: str) -> bool:
    size_b: int = len(string_b)
    doubled_pattern: str = string_b + string_b

    pos_p: int = 0
    max_pos_p: int = len(string_a) - size_b
    while pos_p <= max_pos_p:
        offset_q: int = 0
        while offset_q <= size_b:
            if string_a[pos_p : pos_p + size_b] == doubled_pattern[offset_q : offset_q + size_b]:
                return True
            offset_q += 1
        pos_p += 1

    return False