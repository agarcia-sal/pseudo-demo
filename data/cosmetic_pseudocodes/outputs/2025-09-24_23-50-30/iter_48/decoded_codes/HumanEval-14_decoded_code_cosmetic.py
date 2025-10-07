from typing import Sequence, List, TypeVar

T = TypeVar('T')

def all_prefixes(prm0: Sequence[T]) -> List[Sequence[T]]:
    prm1: List[Sequence[T]] = []
    prm2: int = 0
    while prm2 <= len(prm0) - 1:
        prm3: int = prm2 + 1
        prm4: Sequence[T] = prm0[0:prm3]
        prm1.append(prm4)
        prm2 += 1
    return prm1