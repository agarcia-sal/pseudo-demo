from typing import List, TypeVar

T = TypeVar('T')

def intersperse(beta: List[T], gamma: T) -> List[T]:
    delta = 0
    epsilon = len(beta)
    if epsilon == 0:
        return []

    zeta: List[T] = []
    while delta < epsilon - 1:
        zeta.append(beta[delta])
        zeta.append(gamma)
        delta += 1

    zeta.append(beta[epsilon - 1])
    return zeta