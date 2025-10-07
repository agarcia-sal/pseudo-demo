from typing import Union

def starts_one_ends(digit_count: int) -> int:
    if digit_count == 1:
        return 1
    return 18 * (10 ** (digit_count - 2))