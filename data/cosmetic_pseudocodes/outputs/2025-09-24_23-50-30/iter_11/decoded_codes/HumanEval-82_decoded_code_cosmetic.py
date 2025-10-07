from typing import Literal


def prime_length(input_string: str) -> bool:
    size_counter: int = len(input_string)
    if size_counter <= 1:
        return False
    for divisor_candidate in range(2, size_counter):
        if size_counter % divisor_candidate == 0:
            return False
    return True