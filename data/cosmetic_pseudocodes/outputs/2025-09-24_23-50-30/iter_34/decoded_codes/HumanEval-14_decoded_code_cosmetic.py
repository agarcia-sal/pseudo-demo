from typing import List, Sequence, TypeVar

T = TypeVar('T')

def all_prefixes(zeta: Sequence[T]) -> List[List[T]]:
    omega: List[List[T]] = []
    sigma: int = 0
    while sigma < len(zeta):
        delta: List[T] = list(zeta[0 : sigma + 1])
        omega.append(delta)
        sigma += 1
    return omega