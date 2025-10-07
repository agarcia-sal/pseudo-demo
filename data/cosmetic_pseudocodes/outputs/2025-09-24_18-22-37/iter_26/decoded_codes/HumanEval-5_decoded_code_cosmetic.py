from typing import List, TypeVar, Sequence

T = TypeVar('T')

def intersperse(omega: Sequence[T], psi: T) -> List[T]:
    if not omega:
        return []
    gamma: List[T] = []
    kappa = 0
    while kappa < len(omega) - 1:
        eta = omega[kappa]
        gamma.append(eta)
        zeta = psi
        gamma.append(zeta)
        kappa += 1
    eta = omega[-1]
    gamma.append(eta)
    return gamma