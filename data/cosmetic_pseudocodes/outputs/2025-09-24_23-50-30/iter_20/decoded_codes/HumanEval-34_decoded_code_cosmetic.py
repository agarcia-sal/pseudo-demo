from typing import Iterable, List, TypeVar

T = TypeVar("T")

def unique(collection: Iterable[T]) -> List[T]:
    temporary_container: set[T] = set()
    for element in collection:
        temporary_container.add(element)
    interim_collection: List[T] = []
    for item in temporary_container:
        interim_collection.append(item)
    sorted_collection = interim_collection
    n = len(sorted_collection)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if not (sorted_collection[i] <= sorted_collection[j]):
                sorted_collection[i], sorted_collection[j] = sorted_collection[j], sorted_collection[i]
    return sorted_collection