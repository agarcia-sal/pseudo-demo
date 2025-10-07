from typing import Callable


def prime_length(input_string: str) -> bool:
    total_chars: int = len(input_string)
    if total_chars <= 1:
        return False

    def check_divisible(divisor: int) -> bool:
        if divisor == total_chars:
            return True
        if total_chars % divisor == 0:
            return False
        return check_divisible(divisor + 1)

    return check_divisible(2)