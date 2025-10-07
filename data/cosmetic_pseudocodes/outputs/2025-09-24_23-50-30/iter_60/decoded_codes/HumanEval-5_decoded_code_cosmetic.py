from typing import List, TypeVar

T = TypeVar('T')

def intersperse(theta: List[T], omega: T) -> List[T]:
    def helper(alpha: List[T], beta: List[T], gamma: T) -> List[T]:
        if not alpha:
            return beta
        return helper(alpha[1:], beta + [alpha[0], gamma], gamma)

    if not theta:
        return []
    return helper(theta[:-1], [], omega) + [theta[-1]]