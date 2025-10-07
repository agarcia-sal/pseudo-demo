from typing import Callable

def prime_length(input_string: str) -> bool:
    string_length: int = len(input_string)
    if string_length <= 1:
        return False

    def check_divisor(divisor: int) -> bool:
        if divisor >= string_length:
            return True
        if string_length % divisor == 0:
            return False
        return check_divisor(divisor + 1)

    return check_divisor(2)