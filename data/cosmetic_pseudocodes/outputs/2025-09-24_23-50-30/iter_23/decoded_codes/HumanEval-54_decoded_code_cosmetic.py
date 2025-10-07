from typing import Iterable

def same_chars(tau: Iterable[str], omega: Iterable[str]) -> bool:
    alpha = set(tau)
    beta = set(omega)
    return not (len(alpha - beta) > 0 or len(beta - alpha) > 0)