from typing import Callable


def prime_length(input_string: str) -> bool:
    def inner_check(divisor_current: int, length_val: int) -> bool:
        if divisor_current >= length_val:
            return True
        if length_val % divisor_current == 0:
            return False
        return inner_check(divisor_current + 1, length_val)

    str_len = len(input_string)
    if str_len <= 1:
        return False
    return inner_check(2, str_len)