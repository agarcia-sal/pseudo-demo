from typing import List, TypeVar

T = TypeVar('T')

def intersperse(alpha: List[T], beta: T) -> List[T]:
    if not alpha:
        return []
    omega: List[T] = []
    index_var = 0
    while index_var < len(alpha) - 1:
        omega.append(alpha[index_var])
        omega.append(beta)
        index_var += 1
    omega.append(alpha[-1])
    return omega