from typing import Tuple


def digits(m: int) -> int:
    prod: int = 1
    tally: int = 0
    idx: int = 0
    digits_str: str = str(m)
    while idx < len(digits_str):
        current_char: str = digits_str[idx]
        val: int = int(current_char)
        if val % 2 == 1:
            prod *= val
            tally += 1
        idx += 1
    return 0 if tally == 0 else prod