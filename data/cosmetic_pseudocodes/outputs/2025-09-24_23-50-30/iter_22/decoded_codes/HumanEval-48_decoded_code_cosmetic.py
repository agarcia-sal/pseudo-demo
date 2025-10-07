from typing import Sequence

def is_palindrome(omega: Sequence[str]) -> bool:
    delta: int = len(omega) - 1
    epsilon: int = 0
    while epsilon <= delta:
        if omega[epsilon] != omega[delta]:
            return False
        epsilon += 1
        delta -= 1
    return True