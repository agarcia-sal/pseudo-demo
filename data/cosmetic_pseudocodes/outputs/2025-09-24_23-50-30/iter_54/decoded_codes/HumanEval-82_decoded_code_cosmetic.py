from typing import Callable


def prime_length(input_string: str) -> bool:
    def check_divisor(divisor: int) -> bool:
        if divisor * divisor > len(input_string):
            return True
        if len(input_string) % divisor == 0:
            return False
        return check_divisor(divisor + 1)

    if len(input_string) < 2:
        return False

    return check_divisor(2)