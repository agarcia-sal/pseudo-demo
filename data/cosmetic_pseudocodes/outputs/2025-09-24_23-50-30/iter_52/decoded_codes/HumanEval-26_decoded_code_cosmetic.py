from collections import Counter
from typing import Iterable, TypeVar, List

T = TypeVar('T')

def remove_duplicates(container: Iterable[T]) -> List[T]:
    frequency_map = Counter(container)
    return [item for item in container if frequency_map[item] <= 1]