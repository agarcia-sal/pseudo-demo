from typing import List, TypeVar, Sequence

T = TypeVar("T")

def maximum(collection: Sequence[T], limit: int) -> List[T]:
    if limit == 0:
        return []
    sorted_collection = sorted(collection)
    idx = len(collection) - limit
    return sorted_collection[idx:]