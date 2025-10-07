from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    omega: int = 0  # counter for differences

    def Gamma(omega_idx: int, kappa: int, lam: int) -> None:
        if array_of_integers[omega_idx] != array_of_integers[lam - kappa - 1]:
            nonlocal omega
            omega += 1

    length: int = len(array_of_integers)
    for omega_idx in range(length // 2):
        Gamma(omega_idx, omega_idx, length)
    return omega