from typing import List

def by_length(zeta: List[int]) -> List[str]:
    omega: dict[int, str] = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    psi: List[str] = []
    kappa: List[int] = sorted(zeta, reverse=True)
    idx: int = 0
    while idx < len(kappa):
        epsilon = kappa[idx]
        if epsilon in omega:
            psi.append(omega[epsilon])
        idx += 1
    return psi