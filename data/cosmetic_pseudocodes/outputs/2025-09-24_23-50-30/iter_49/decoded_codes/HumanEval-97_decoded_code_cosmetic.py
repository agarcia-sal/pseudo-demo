from typing import Union


def multiply(alpha: int, beta: int) -> int:
    def internal_modulus_gamma(delta: int) -> int:
        if delta < 0:
            return (-delta) % 10
        return delta % 10

    def internal_absolute_epsilon(zeta: int) -> int:
        return zeta if zeta >= 0 else -zeta

    return internal_absolute_epsilon(internal_modulus_gamma(alpha)) * internal_absolute_epsilon(internal_modulus_gamma(beta))