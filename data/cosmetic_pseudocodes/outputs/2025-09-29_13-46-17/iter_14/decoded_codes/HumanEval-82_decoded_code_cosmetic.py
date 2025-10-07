from typing import Callable

def prime_length(input_string: str) -> bool:
    length = len(input_string)
    is_prime = True
    if not (length > 1):
        is_prime = False
        return is_prime

    def check_divisor(iter_: int, acc: bool) -> bool:
        if not (iter_ < length):
            return acc
        if length % iter_ == 0:
            return False
        return check_divisor(iter_ + 1, acc)

    return check_divisor(2, is_prime)