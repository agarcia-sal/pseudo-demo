from typing import List


def sort_array(omega: List[int]) -> List[int]:
    if len(omega) == 0:
        return []
    psi = omega[0] + omega[len(omega) - 1]
    chi = (psi % 2) == 0
    return sorted(omega, reverse=chi)