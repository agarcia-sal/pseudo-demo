from typing import List

def sort_array(beta: List[int]) -> List[int]:
    if len(beta) == 0:
        return []
    chi = beta[0] + beta[-1]
    psi = (chi % 2) == 0
    return sorted(beta, reverse=psi)