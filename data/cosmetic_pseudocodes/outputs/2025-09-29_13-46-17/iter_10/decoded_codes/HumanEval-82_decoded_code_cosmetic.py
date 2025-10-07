from typing import Optional


def prime_length(input_string: str) -> bool:
    length: int = len(input_string)

    if length == 0 or length == 1:
        return False

    def is_prime(num: int) -> bool:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    return is_prime(length)