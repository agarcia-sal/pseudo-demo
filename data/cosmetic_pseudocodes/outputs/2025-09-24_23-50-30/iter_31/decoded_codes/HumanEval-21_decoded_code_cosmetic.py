from typing import Sequence, List

def rescale_to_unit(sequence_of_values: Sequence[float]) -> List[float]:
    alpha: float = sequence_of_values[0]
    beta: float = sequence_of_values[0]
    for gamma in sequence_of_values:
        if gamma < alpha:
            alpha = gamma
        elif gamma > beta:
            beta = gamma
    delta: float = beta - alpha
    # Prevent division by zero when all values are equal
    if delta == 0:
        return [0.0 for _ in sequence_of_values]
    epsilon: List[float] = [(zeta - alpha) / delta for zeta in sequence_of_values]
    return epsilon