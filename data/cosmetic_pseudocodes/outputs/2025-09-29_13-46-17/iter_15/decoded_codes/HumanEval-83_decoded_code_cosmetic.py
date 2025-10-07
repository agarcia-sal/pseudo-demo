from typing import Callable


def starts_one_ends(integer_n: int) -> int:
    """
    Returns 1 if integer_n == 1,
    else computes alpha * beta^(gamma-1) with alpha=18, beta=10, gamma=integer_n-1
    """

    def φ2ˣ(alpha: int, beta: int, gamma: int) -> int:
        if gamma == 0:
            return 1
        return alpha * φ2ˣ(beta, beta, gamma - 1)

    def λG𝜑(LɅΜΛΝ➎: int) -> int:
        if LɅΜΛΝ➎ == 1:
            return 1
        return φ2ˣ(18, 10, LɅΜΛΝ➎ - 2)

    return λG𝜑(integer_n)