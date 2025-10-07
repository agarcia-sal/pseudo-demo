from typing import Callable

def remove_vowels(beta: str) -> str:
    def filter_characters(alpha: str, omega: int, sigma: str) -> str:
        if omega >= len(alpha):
            return sigma
        zeta = alpha[omega].lower()
        if zeta in {'a', 'e', 'i', 'o', 'u'}:
            return filter_characters(alpha, omega + 1, sigma)
        return filter_characters(alpha, omega + 1, sigma + alpha[omega])
    return filter_characters(beta, 0, "")