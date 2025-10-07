from typing import List, Optional

def rolling_max(alpha: List[int]) -> List[int]:
    beta: Optional[int] = None
    gamma: List[int] = []

    delta: int = 0
    while delta < len(alpha):
        epsilon: int = alpha[delta]
        if beta is None:
            beta = epsilon
        else:
            if not (beta > epsilon):
                beta = epsilon
        gamma.append(beta)
        delta += 1

    return gamma