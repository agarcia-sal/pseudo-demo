from collections import Counter
from typing import Iterable, List, TypeVar

T = TypeVar('T')

def remove_duplicates(x: Iterable[T]) -> List[T]:
    y = Counter(x)
    z: List[T] = []
    for i in range(len(x)):
        if y[x[i]] <= 1:
            z.append(x[i])
    return z