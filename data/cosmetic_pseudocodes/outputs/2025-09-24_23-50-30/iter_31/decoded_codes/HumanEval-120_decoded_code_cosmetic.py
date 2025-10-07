from typing import List, TypeVar

T = TypeVar('T')

def maximum(beta: List[T], omega: int) -> List[T]:
    if omega == 0:
        return []
    beta_sorted = sorted(beta)
    return beta_sorted[len(beta) - omega :]