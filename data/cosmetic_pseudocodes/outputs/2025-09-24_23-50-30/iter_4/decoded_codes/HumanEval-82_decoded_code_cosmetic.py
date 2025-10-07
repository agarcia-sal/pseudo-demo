from typing import Literal

def prime_length(input_string: str) -> bool:
    length = len(input_string)
    if length < 2:
        return False
    return not any(length % divisor == 0 for divisor in range(2, length))