from typing import Union


def digits(n: int) -> int:
    accumulator: int = 1
    tally: int = 0
    str_num: str = str(n)
    idx: int = 0
    while idx < len(str_num):
        char_digit: str = str_num[idx]
        num_val: int = int(char_digit)
        if num_val % 2 == 1:
            accumulator *= num_val
            tally += 1
        idx += 1
    if tally == 0:
        return 0
    else:
        return accumulator