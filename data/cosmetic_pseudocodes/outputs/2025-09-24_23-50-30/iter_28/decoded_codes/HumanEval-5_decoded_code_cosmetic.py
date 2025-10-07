from typing import List, TypeVar

T = TypeVar('T')

def intersperse(alpha: List[T], omega: T) -> List[T]:
    def zeta(beta: List[T], gamma: List[T], delta: int) -> List[T]:
        if delta >= len(beta):
            return gamma
        epsilon = beta[delta]
        zeta_result = gamma + [epsilon, omega]
        return zeta(beta, zeta_result, delta + 1)

    if len(alpha) == 0:
        return []
    if len(alpha) == 1:
        return [alpha[0]]
    theta = zeta(alpha, [], 0)
    return theta[:-1]