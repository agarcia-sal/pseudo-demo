from typing import Union

def prime_length(string: str) -> bool:
    length: int = len(string)
    if length < 2:
        return False
    for i in range(2, length):
        if length % i == 0:
            return False
    return True