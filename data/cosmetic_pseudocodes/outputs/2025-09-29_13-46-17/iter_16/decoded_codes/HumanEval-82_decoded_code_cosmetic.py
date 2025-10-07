from typing import Callable

def prime_length(input_string: str) -> bool:
    length: int = len(input_string)

    if length <= 1:
        return False

    def inner_check(divisor: int, number: int) -> bool:
        if divisor < number:
            if number % divisor == 0:
                return False
            else:
                return inner_check(divisor + 1, number)
        else:
            return True

    return inner_check(2, length)