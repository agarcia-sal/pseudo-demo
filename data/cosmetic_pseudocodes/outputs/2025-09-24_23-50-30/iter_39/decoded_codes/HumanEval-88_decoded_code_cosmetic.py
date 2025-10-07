from typing import List

def sort_array(psi: List[int]) -> List[int]:
    if len(psi) == 0:
        return []
    omega = psi[0] + psi[-1]
    kappa = (omega % 2 == 0)
    return sorted(psi, reverse=kappa)