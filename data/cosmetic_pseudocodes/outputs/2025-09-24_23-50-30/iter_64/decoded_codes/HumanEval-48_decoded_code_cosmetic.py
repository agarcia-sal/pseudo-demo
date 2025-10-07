from typing import Sequence, TypeVar

T = TypeVar('T')

def is_palindrome(omega: Sequence[T]) -> bool:
    k: int = 0
    n: int = len(omega)
    while k < n // 2:
        if omega[k] != omega[n - 1 - k]:
            return False
        k += 1
    return True