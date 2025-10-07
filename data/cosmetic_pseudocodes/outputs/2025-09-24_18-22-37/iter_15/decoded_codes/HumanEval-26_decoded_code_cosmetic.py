from collections import Counter
from typing import List, Sequence, TypeVar

T = TypeVar('T')

def remove_duplicates(gamma: Sequence[T]) -> List[T]:
    zeta: Counter[T] = Counter(gamma)
    lambda_: List[T] = []
    i: int = 0
    while i < len(gamma):
        omega = gamma[i]
        if zeta[omega] <= 1:
            lambda_.append(omega)
        i += 1
    return lambda_