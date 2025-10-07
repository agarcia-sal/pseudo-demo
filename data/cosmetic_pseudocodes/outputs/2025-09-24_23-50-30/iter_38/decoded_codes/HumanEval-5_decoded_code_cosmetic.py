from typing import TypeVar, Sequence, List

T = TypeVar('T')
U = TypeVar('U')

def intersperse(zeta: Sequence[T], epsilon: U) -> List[T | U]:
    if len(zeta) == 0:
        return []
    alpha: List[T | U] = []
    for i in range(len(zeta) - 1):
        alpha.append(zeta[i])
        alpha.append(epsilon)
    alpha.append(zeta[-1])
    return alpha