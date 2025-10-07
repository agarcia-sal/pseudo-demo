from typing import List, TypeVar

T = TypeVar('T')

def intersperse(alpha: List[T], omega: T) -> List[T]:
    def helper(beta: List[T], gamma: List[T], delta: List[T]) -> List[T]:
        if not beta:
            return delta
        epsilon, *zeta = beta
        if not gamma:
            return delta + [epsilon]
        return helper(zeta, gamma[1:], delta + [epsilon, omega])
    return helper(alpha, alpha[1:], [])