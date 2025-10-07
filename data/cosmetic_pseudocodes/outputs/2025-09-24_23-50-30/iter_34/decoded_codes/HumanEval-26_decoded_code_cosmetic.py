from collections import Counter
from typing import Iterable, List, TypeVar

T = TypeVar('T')

def remove_duplicates(alpha: Iterable[T]) -> List[T]:
    beta: Counter[T] = Counter(alpha)
    return [gamma for gamma in alpha if beta[gamma] <= 1]