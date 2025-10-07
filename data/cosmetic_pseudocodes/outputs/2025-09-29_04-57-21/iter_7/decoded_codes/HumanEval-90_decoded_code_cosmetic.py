from typing import Optional, Iterable, TypeVar, List

T = TypeVar('T', bound='SupportsLessThan')

class SupportsLessThan:
    def __lt__(self, other: object) -> bool:
        ...

def next_smallest(numbers_collection: Iterable[T]) -> Optional[T]:
    filtered_unique: List[T] = sorted(set(numbers_collection))
    if len(filtered_unique) < 2:
        return None
    return filtered_unique[1]