from typing import List, TypeVar

T = TypeVar('T')

def intersperse(alpha: List[T], beta: T) -> List[T]:
    omega: List[T] = []
    if len(alpha) > 0:
        for i in range(len(alpha) - 1):
            omega.append(alpha[i])
            omega.append(beta)
        omega.append(alpha[-1])
    return omega