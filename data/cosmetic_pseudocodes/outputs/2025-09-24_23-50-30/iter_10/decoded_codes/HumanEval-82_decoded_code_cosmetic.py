from typing import Literal


def prime_length(input_string: str) -> bool:
    str_len: int = len(input_string)
    while True:
        if str_len == 0 or str_len == 1:
            return False
        break

    for divisor_candidate in range(2, str_len):
        if (str_len - (str_len // divisor_candidate) * divisor_candidate) == 0:
            return False
    return True