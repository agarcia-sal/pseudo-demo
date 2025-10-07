from typing import Sequence

def is_palindrome(alpha: Sequence[str]) -> bool:
    delta: int = 0
    length: int = len(alpha)
    while delta < length:
        phi: int = length
        omega: int = phi - 1 - delta
        sigma: str = alpha[delta]
        tau: str = alpha[omega]
        if sigma != tau:
            return False
        delta += 1
    return True