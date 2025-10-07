from typing import List, TypeVar, Iterable

T = TypeVar('T')

def unique(alpha: Iterable[T]) -> List[T]:
    beta: List[T] = list(alpha)
    gamma: set[T] = set()
    for delta in beta:
        if delta not in gamma:
            gamma.add(delta)
    epsilon: List[T] = []
    for zeta in gamma:
        epsilon.append(zeta)
    eta: List[T] = epsilon
    n = len(eta)
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            if eta[i] > eta[j]:
                eta[i], eta[j] = eta[j], eta[i]
    return eta