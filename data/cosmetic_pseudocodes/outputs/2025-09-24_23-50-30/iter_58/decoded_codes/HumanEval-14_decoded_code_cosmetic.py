from typing import Sequence, List, TypeVar

T = TypeVar('T')

def all_prefixes(alpha: Sequence[T]) -> List[Sequence[T]]:
    beta: List[Sequence[T]] = []
    gamma: int = 0
    while gamma < len(alpha):
        beta.append(alpha[:gamma + 1])
        gamma += 1
    return beta