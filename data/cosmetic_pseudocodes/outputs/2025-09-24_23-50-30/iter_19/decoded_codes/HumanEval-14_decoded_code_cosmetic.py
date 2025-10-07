from typing import List, Sequence, TypeVar

T = TypeVar('T')

def all_prefixes(alpha: Sequence[T]) -> List[Sequence[T]]:
    omega: List[Sequence[T]] = []
    theta: int = 0
    while theta < len(alpha):
        omega.append(alpha[:theta + 1])
        theta += 1
    return omega