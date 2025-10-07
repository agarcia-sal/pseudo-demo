from typing import AnyStr

def prime_length(string: AnyStr) -> bool:
    length: int = len(string)
    if length <= 1:
        return False
    for i in range(2, length):
        if length % i == 0:
            return False
    return True