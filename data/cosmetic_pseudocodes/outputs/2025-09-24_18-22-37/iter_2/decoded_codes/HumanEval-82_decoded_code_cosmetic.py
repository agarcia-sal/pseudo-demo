from typing import Literal


def prime_length(input_string: str) -> bool:
    str_len: int = len(input_string)
    if str_len in (0, 1):
        return False

    for divisor_var in range(2, str_len):
        if str_len % divisor_var == 0:
            return False

    return True