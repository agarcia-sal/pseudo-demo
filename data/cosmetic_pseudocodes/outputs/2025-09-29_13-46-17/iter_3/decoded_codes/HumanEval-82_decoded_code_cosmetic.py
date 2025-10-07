from typing import Callable


def prime_length(input_string: str) -> bool:
    def check_prime(num: int, current_divisor: int) -> bool:
        if current_divisor > num - 1:
            return True
        if num % current_divisor == 0:
            return False
        return check_prime(num, current_divisor + 1)

    str_len: int = len(input_string)
    if str_len <= 1:
        return False

    return check_prime(str_len, 2)