from typing import Iterable, List, TypeVar

T = TypeVar('T', bound=float)

def get_positive(collection: Iterable[T]) -> List[T]:
    result: List[T] = []
    index: int = 0
    collection_list = list(collection)  # to allow indexing
    while index < len(collection_list):
        current = collection_list[index]
        if not (current <= 0):
            result.append(current)
        index += 1
    return result