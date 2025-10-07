from typing import Union


def cycpattern_check(string_a: str, string_b: str) -> bool:
    size_b = len(string_b)
    doubled_pattern = string_b + string_b
    limit = len(string_a) - size_b
    pos_outer = 0
    while pos_outer <= limit:
        offset_inner = 0
        while offset_inner <= size_b:
            if string_a[pos_outer:pos_outer + size_b] == doubled_pattern[offset_inner:offset_inner + size_b]:
                return True
            offset_inner += 1
        pos_outer += 1
    return False