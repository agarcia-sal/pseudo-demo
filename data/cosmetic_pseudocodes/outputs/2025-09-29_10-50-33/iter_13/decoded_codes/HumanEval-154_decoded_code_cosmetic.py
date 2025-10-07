from typing import Union


def cycpattern_check(string_a: str, string_b: str) -> bool:
    b_length: int = len(string_b)
    double_pattern: str = string_b + string_b

    i: int = 0
    while i <= len(string_a) - b_length:
        j: int = 0
        while j <= b_length:
            if string_a[i : i + b_length] == double_pattern[j : j + b_length]:
                return True
            j += 1
        i += 1

    return False