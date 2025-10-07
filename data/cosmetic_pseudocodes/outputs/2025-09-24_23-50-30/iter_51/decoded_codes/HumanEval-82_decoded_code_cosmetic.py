from typing import Callable


def prime_length(string_param: str) -> bool:
    def divisor_check(index_var: int) -> bool:
        if index_var >= len(string_param) - 1:
            return True
        if len(string_param) % index_var == 0:
            return False
        return divisor_check(index_var + 1)

    str_len = len(string_param)
    if str_len == 0 or str_len == 1:
        return False
    return divisor_check(2)