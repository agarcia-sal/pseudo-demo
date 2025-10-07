from typing import Dict

def histogram(zeta: str) -> Dict[str, int]:
    def count_occurrences(arr: list[str], val: str) -> int:
        return sum(1 for x in arr if x == val)

    omega: Dict[str, int] = {}
    chi: list[str] = zeta.split(" ")
    nu: int = 0

    for sigma in chi:
        if sigma != "":
            occ = count_occurrences(chi, sigma)
            if occ > nu:
                nu = occ

    if nu > 0:
        for rho in chi:
            if count_occurrences(chi, rho) == nu:
                omega[rho] = nu

    return omega