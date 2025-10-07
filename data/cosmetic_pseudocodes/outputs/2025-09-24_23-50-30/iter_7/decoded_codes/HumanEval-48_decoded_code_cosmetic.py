from typing import Sequence, TypeVar

T = TypeVar('T', bound=Sequence)

def is_palindrome(x: T) -> bool:
    i: int = 0
    j: int = len(x) - 1
    while i < j:
        if x[j] != x[i]:
            return False
        j -= 1
        i += 1
    return True