from typing import Callable


def is_palindrome(omega: str) -> bool:
    def iterate_phi(delta: int) -> bool:
        if delta < len(omega):
            if omega[delta] != omega[len(omega) - 1 - delta]:
                return False
            return iterate_phi(delta + 1)
        return True
    return iterate_phi(0)