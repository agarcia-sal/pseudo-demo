from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(zeta: Iterable[T]) -> List[T]:
    alpha = set()
    for phi in zeta:
        alpha.add(phi)
    beta = list(alpha)
    gamma = sorted(beta)
    return gamma