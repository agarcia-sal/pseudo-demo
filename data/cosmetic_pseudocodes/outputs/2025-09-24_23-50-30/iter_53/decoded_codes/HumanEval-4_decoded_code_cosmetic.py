from typing import Sequence

def mean_absolute_deviation(alpha: Sequence[float]) -> float:
    sigma: int = len(alpha)
    if sigma == 0:
        raise ValueError("Input sequence must not be empty")

    gamma: float = sum(alpha) / sigma  # mean of alpha
    delta: float = sum(abs(x - gamma) for x in alpha)  # sum of absolute deviations

    return delta / sigma