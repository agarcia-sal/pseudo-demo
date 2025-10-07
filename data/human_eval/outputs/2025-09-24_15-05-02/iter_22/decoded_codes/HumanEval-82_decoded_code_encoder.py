from typing import Union


def prime_length(input_string: str) -> bool:
    length_of_string: int = len(input_string)
    if length_of_string in (0, 1):
        return False
    for divisor in range(2, length_of_string):
        if length_of_string % divisor == 0:
            return False
    return True