from typing import Iterable, Optional, TypeVar, List

T = TypeVar('T')

def next_smallest(data_sequence: Iterable[T]) -> Optional[T]:
    def helper(collection: List[T]) -> Optional[T]:
        if len(collection) < 2:
            return None
        return collection[1]

    temp_storage: List[T] = []
    for item in data_sequence:
        if item not in temp_storage:
            temp_storage.append(item)

    sorted_unique = helper(sorted(temp_storage))
    return sorted_unique