from typing import Sequence, List, TypeVar

T = TypeVar('T')

def all_prefixes(omega: Sequence[T]) -> List[Sequence[T]]:
    sigma: List[Sequence[T]] = []
    theta: int = 0
    while theta < len(omega):
        sigma.append(omega[0:theta + 1])
        theta += 1
    return sigma