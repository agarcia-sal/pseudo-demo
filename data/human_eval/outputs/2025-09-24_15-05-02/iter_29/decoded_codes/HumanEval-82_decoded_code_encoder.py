from typing import AnyStr

def prime_length(input_string: AnyStr) -> bool:
    length_of_string: int = len(input_string)
    if length_of_string <= 1:
        return False
    for divisor in range(2, length_of_string):
        if length_of_string % divisor == 0:
            return False
    return True