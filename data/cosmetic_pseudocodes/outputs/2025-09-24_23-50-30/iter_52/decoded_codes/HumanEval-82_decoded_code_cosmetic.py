from typing import Callable

def prime_length(input_string: str) -> bool:
    def helper(current_divisor: int) -> bool:
        length = len(input_string)
        if current_divisor >= length:
            return True
        if length % current_divisor == 0:
            return False
        return helper(current_divisor + 1)

    if len(input_string) <= 1:
        return False

    return helper(2)