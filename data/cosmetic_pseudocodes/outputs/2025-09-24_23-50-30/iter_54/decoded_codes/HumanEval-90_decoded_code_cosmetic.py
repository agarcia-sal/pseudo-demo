from typing import Optional, Iterable, TypeVar, List

T = TypeVar('T', bound=int)

def next_smallest(nums_collection: Iterable[T]) -> Optional[T]:
    tmp_set: set[T] = set()
    for n in nums_collection:
        tmp_set.add(n)
    sorted_unique: List[T] = sorted(tmp_set)
    if len(sorted_unique) < 2:
        return None
    return sorted_unique[1]