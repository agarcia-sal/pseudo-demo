from typing import Sequence, List, TypeVar

T = TypeVar('T', bound=object)

def common(alpha: Sequence[T], beta: Sequence[T]) -> List[T]:
    gamma: set[T] = set()
    delta: int = 0
    while delta < len(alpha):
        epsilon: int = 0
        while epsilon < len(beta):
            zeta: T = alpha[delta]
            eta: T = beta[epsilon]
            if zeta == eta:
                gamma.add(zeta)
            epsilon += 1
        delta += 1
    theta: List[T] = sorted(gamma)
    return theta