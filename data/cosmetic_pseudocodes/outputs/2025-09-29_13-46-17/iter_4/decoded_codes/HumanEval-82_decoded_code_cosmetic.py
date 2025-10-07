from typing import Callable


def prime_length(input_string: str) -> bool:
    def check_divisor(current_divisor: int, max_divisor: int) -> bool:
        if current_divisor >= max_divisor:
            return True
        if len(input_string) % current_divisor == 0:
            return False
        return check_divisor(current_divisor + 1, max_divisor)

    len_val: int = len(input_string)
    if not (len_val > 1):
        return False
    return check_divisor(2, len_val)