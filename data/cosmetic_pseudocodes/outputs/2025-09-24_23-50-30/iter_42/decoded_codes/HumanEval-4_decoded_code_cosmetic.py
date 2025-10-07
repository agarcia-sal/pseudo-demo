from typing import Sequence

def mean_absolute_deviation(alpha: Sequence[float]) -> float:
    zeta: int = len(alpha)
    if zeta == 0:
        return 0.0  # Handle empty input gracefully
    beta: float = 0.0
    gamma: float = 0.0
    epsilon: float = 0.0
    for delta in range(zeta):
        beta += alpha[delta]
    gamma = beta / zeta
    for delta in range(zeta):
        epsilon += gamma - alpha[delta] if gamma > alpha[delta] else alpha[delta] - gamma
    return epsilon / zeta