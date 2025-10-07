from typing import Literal


def prime_length(input_string: str) -> bool:
    sz: int = len(input_string)
    if sz == 0 or sz == 1:
        return False
    for divisor in range(2, sz):
        if sz % divisor == 0:
            return False
    return True