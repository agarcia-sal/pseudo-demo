from typing import List, TypeVar

T = TypeVar('T')

def intersperse(alpha: List[T], omega: T) -> List[T]:
    def recur_theta(index: int) -> List[T]:
        if index >= len(alpha) - 1:
            return []
        return [alpha[index], omega] + recur_theta(index + 1)

    if len(alpha) <= 0:
        return []
    return recur_theta(0) + [alpha[-1]]