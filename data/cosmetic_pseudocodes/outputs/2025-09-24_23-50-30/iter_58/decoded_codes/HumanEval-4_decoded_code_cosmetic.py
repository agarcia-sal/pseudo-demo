from typing import Sequence

def mean_absolute_deviation(alpha: Sequence[float]) -> float:
    n = len(alpha)
    if n == 0:
        raise ValueError("Input sequence must not be empty")
    beta = sum(alpha) / n  # mean of alpha
    gamma = 0.0
    delta = 0
    while delta < n:
        gamma += abs(alpha[delta] - beta)
        delta += 1
    epsilon = gamma / n  # mean absolute deviation
    return epsilon