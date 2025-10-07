from typing import List

def string_sequence(kappa: int) -> str:
    zeta: List[str] = []
    theta: int = 0
    while theta <= kappa:
        iota: str = str(theta)
        zeta.append(iota)
        theta += 1
    lambda_: str = ""
    mu: int = 0
    nu: int = len(zeta)
    while mu < nu:
        if mu == nu - 1:
            lambda_ += zeta[mu]
        else:
            lambda_ += zeta[mu] + " "
        mu += 1
    return lambda_