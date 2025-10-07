from typing import Callable


def prime_length(input_string: str) -> bool:
    count: int = 0
    while count < len(input_string):
        count += 1

    if count == 0 or count == 1:
        return False

    def check_divisor(divisor: int, length_val: int) -> bool:
        if divisor >= length_val:
            return True
        if length_val % divisor == 0:
            return False
        return check_divisor(divisor + 1, length_val)

    return check_divisor(2, count)