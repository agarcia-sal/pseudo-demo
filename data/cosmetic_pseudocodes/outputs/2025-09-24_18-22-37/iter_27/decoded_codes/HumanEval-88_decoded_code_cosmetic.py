from typing import List


def sort_array(alpha: List[int]) -> List[int]:
    beta: int = len(alpha)
    if beta != 0:
        gamma: int = alpha[0]
        delta: int = alpha[beta - 1]
        epsilon: int = gamma + delta
        zeta: bool = (epsilon % 2) == 0
        eta: List[int] = alpha.copy()
        eta.sort(reverse=not zeta)  # If zeta is True (even), sort ascending; else descending
        return eta
    else:
        return []