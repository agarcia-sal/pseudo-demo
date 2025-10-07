from typing import List, TypeVar

T = TypeVar('T')

def intersperse(alpha: List[T], beta: T) -> List[T]:
    if not alpha:
        return []
    omega: List[T] = []
    idx = 0
    while idx < len(alpha) - 1:
        omega.append(alpha[idx])
        omega.append(beta)
        idx += 1
    omega.append(alpha[-1])
    return omega