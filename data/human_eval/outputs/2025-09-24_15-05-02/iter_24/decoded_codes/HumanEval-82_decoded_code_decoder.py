from typing import Union

def prime_length(input_string: str) -> bool:
    length: int = len(input_string)
    if length <= 1:
        return False
    for i in range(2, int(length ** 0.5) + 1):  # Check divisors up to sqrt(length)
        if length % i == 0:
            return False
    return True