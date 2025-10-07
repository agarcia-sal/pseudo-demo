from typing import List, Optional

def rolling_max(alpha: List[int]) -> List[int]:
    beta: Optional[int] = None
    gamma: List[int] = []
    delta: int = 0
    while delta < len(alpha):
        beta_isnull: bool = (beta is None)
        if beta_isnull:
            beta = alpha[delta]
        else:
            epsilon: int = beta
            zeta: int = alpha[delta]
            if epsilon > zeta:
                beta = epsilon
            else:
                beta = zeta
        gamma.append(beta)
        delta += 1
    return gamma