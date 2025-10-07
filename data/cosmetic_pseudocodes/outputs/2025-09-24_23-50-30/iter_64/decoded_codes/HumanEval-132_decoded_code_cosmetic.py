from typing import Sequence

def is_nested(alpha: Sequence[str]) -> bool:
    omega: list[int] = []
    psi: list[int] = []
    i = 0

    while i < len(alpha):
        if alpha[i] == '[':
            omega.append(i)
        else:
            psi.append(i)
        i += 1

    psi.reverse()

    rho = 0
    sigma = 0
    tau = len(psi)

    for zeta in omega:
        if sigma < tau and zeta < psi[sigma]:
            rho += 1
            sigma += 1

    return rho >= 2