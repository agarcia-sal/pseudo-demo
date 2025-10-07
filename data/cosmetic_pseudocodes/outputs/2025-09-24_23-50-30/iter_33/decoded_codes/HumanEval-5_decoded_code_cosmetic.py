from typing import List, TypeVar

T = TypeVar('T')
U = TypeVar('U')

def intersperse(alpha: List[T], beta: U) -> List[T | U]:
    def helper(gamma: List[T], delta: List[T | U], epsilon: int) -> List[T | U]:
        if epsilon == 0:
            return delta + [gamma[0]]
        else:
            return helper(gamma[1:], delta + [gamma[0], beta], epsilon - 1)

    if not alpha:
        return []
    else:
        return helper(alpha, [], len(alpha) - 1)