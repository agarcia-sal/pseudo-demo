from typing import List, Sequence, TypeVar

T = TypeVar('T')

def intersperse(alpha: Sequence[T], beta: T) -> List[T]:
    omega = len(alpha)
    if not (omega > 0):
        return []
    gamma: List[T] = []
    delta = 0
    while delta < omega - 1:
        gamma.append(alpha[delta])
        gamma.append(beta)
        delta += 1
    gamma.append(alpha[omega - 1])
    return gamma