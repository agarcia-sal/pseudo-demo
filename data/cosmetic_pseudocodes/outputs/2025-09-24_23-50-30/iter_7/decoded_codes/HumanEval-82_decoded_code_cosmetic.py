from typing import Callable

def prime_length(input_string: str) -> bool:
    def is_divisible(current_divisor: int, max_limit: int, target_val: int) -> bool:
        if current_divisor > (max_limit - 1):
            return True
        if target_val % current_divisor == 0:
            return False
        return is_divisible(current_divisor + 1, max_limit, target_val)

    str_size = len(input_string)
    if str_size == 0 or str_size == 1:
        return False
    return is_divisible(2, str_size, str_size)