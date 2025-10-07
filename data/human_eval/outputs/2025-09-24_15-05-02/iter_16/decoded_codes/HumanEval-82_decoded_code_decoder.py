from typing import Optional

def prime_length(input_string: str) -> bool:
    length: int = len(input_string)
    if length == 0 or length == 1:
        return False
    for i in range(2, length):
        if length % i == 0:
            return False
    return True