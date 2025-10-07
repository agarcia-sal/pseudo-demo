from typing import Callable

def multiply(alpha: int, beta: int) -> int:
    def gamma(delta: int) -> int:
        return -delta if delta < 0 else delta

    def epsilon(zeta: int) -> int:
        theta = zeta - (zeta // 10) * 10
        return -theta if theta < 0 else theta

    return gamma(epsilon(alpha)) * gamma(epsilon(beta))