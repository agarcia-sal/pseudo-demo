from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(alpha: Iterable[T]) -> List[T]:
    beta: dict[T, bool] = {}
    for gamma in alpha:
        beta[gamma] = True
    delta: List[T] = []
    for epsilon in beta:
        delta.append(epsilon)
    zeta: List[T] = delta
    n = len(zeta)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if zeta[j] > zeta[j + 1]:
                eta = zeta[j]
                zeta[j] = zeta[j + 1]
                zeta[j + 1] = eta
    return zeta