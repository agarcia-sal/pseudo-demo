from typing import Sequence

def has_close_elements(sequence_alpha: Sequence[float], epsilon: float) -> bool:
    length = len(sequence_alpha)
    for gamma in range(length):
        for delta in range(length):
            if gamma == delta:
                continue
            sigma = sequence_alpha[gamma] - sequence_alpha[delta]
            tau = sigma if sigma >= 0 else -sigma
            if tau < epsilon:
                return True
    return False