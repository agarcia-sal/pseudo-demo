from typing import Union

def is_prime(x: int) -> bool:
    if x < 2:
        return False
    c = 2
    while c <= x - 2:
        if x % c == 0:
            return False
        c += 1
    return True