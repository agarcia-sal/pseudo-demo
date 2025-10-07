from typing import Iterable

def same_chars(x_alpha: Iterable[str], x_beta: Iterable[str]) -> bool:
    y_gamma = set(x_alpha)
    z_delta = set(x_beta)
    return (y_gamma - z_delta == set()) and (z_delta - y_gamma == set())