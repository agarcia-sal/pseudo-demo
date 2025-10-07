from typing import Sequence


def cycpattern_check(string_a: str, string_b: str) -> bool:
    b_size: int = len(string_b)
    doubled_pattern: str = string_b + string_b
    max_start: int = len(string_a) - b_size
    start_pos: int = 0
    while start_pos <= max_start:
        cursor: int = 0
        while cursor <= b_size:
            if string_a[start_pos : start_pos + b_size] == doubled_pattern[cursor : cursor + b_size]:
                return True
            cursor += 1
        start_pos += 1
    return False