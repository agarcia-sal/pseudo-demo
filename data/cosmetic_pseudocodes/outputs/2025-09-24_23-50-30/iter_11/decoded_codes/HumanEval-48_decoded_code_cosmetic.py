from typing import Sequence, TypeVar

T = TypeVar('T')

def is_palindrome(beta: Sequence[T]) -> bool:
    delta: int = len(beta) - 1
    epsilon: int = 0
    while epsilon <= delta / 2:
        if beta[epsilon] != beta[delta - epsilon]:
            return False
        epsilon += 1
    return True