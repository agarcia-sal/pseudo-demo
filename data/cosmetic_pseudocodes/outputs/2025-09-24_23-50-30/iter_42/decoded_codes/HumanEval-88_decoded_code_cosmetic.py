from typing import List


def sort_array(alpha: List[int]) -> List[int]:
    length: int = len(alpha)
    if length == 0:
        return []
    epsilon: int = length - 1
    gamma: int = alpha[0] + alpha[epsilon]
    zeta: bool = (gamma % 2 == 0)
    kappa: List[int] = sorted(alpha)
    return kappa[::-1] if zeta else kappa