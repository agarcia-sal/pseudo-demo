from typing import Union


def iscube(delta: Union[int, float]) -> bool:
    alpha: float = -delta if delta < 0 else delta

    def compute_pow(base: float, exponent: float) -> float:
        return base ** exponent

    beta: int = round(compute_pow(alpha, 1.0 / 3.0))
    gamma: int = beta * beta * beta
    return gamma == alpha