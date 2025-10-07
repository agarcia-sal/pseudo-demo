from typing import Any


def circular_shift(alpha: Any, beta: int) -> str:
    gamma: str = str(alpha)
    delta: int = len(gamma)
    if beta > delta:
        return gamma[::-1]  # reverse string
    else:
        epsilon: str = gamma[delta - beta : delta]
        zeta: str = gamma[0 : delta - beta]
        return epsilon + zeta