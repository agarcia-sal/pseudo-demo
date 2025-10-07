from typing import Literal

def cycpattern_check(string_a: str, string_b: str) -> bool:
    needle_len: int = len(string_b)
    doubled_pattern: str = string_b + string_b

    outer_pos: int = 0
    while outer_pos <= len(string_a) - needle_len:
        inner_pos: int = 0
        while inner_pos <= needle_len:
            if string_a[outer_pos : outer_pos + needle_len] == doubled_pattern[inner_pos : inner_pos + needle_len]:
                return True  # abort with True
            inner_pos += 1
        outer_pos += 1

    return False  # abort with False