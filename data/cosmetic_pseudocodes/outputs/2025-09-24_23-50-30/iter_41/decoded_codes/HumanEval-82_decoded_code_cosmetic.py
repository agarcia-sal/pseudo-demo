from typing import Callable


def prime_length(input_string: str) -> bool:
    def divisor_check(current_divisor: int, max_divisor: int, str_len: int, is_prime_flag: bool) -> bool:
        if current_divisor > max_divisor:
            return is_prime_flag
        match str_len % current_divisor:
            case 0:
                return False
            case _:
                return divisor_check(current_divisor + 1, max_divisor, str_len, is_prime_flag)

    str_len = len(input_string)
    if not (str_len > 1):
        return False
    return divisor_check(2, str_len - 1, str_len, True)