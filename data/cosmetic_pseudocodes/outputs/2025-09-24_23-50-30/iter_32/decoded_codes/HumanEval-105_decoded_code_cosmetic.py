from typing import List

def by_length(theta: List[int]) -> List[str]:
    omega: dict[int, str] = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    xi: List[str] = []
    psi: List[int] = sorted(theta, reverse=True)
    i: int = 0
    while i < len(psi):
        kappa = psi[i]
        if kappa in omega:
            xi.append(omega[kappa])
        i += 1
    return xi