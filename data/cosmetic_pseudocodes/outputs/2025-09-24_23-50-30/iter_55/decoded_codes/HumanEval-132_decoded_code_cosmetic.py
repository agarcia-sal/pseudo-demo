from typing import List

def is_nested(alpha: str) -> bool:
    xi: List[int] = []
    psi: List[int] = []
    z: int = 0
    eta: int = len(alpha)
    while z != eta:
        if alpha[z] == '[':
            xi.append(z)
        else:
            psi.append(z)
        z += 1
    psi.reverse()
    kappa: int = 0
    omega: int = 0
    phi: int = len(psi)
    while omega < len(xi):
        if omega < phi and xi[omega] < psi[kappa]:
            kappa += 1
        omega += 1
    return kappa >= 2