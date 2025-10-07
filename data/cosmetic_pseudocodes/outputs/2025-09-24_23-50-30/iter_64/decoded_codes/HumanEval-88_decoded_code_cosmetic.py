from typing import List

def sort_array(zeta: List[int]) -> List[int]:
    if len(zeta) == 0:
        return []
    beta: int = zeta[0] + zeta[-1]
    gamma: bool = (beta % 2) == 0
    return sorted(zeta, reverse=gamma)