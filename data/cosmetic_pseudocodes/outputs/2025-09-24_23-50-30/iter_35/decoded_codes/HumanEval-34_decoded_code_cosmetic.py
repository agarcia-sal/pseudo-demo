from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(collection: Iterable[T]) -> List[T]:
    uniqueSet = set(collection)  # Efficiently add all elements to set to get unique elements
    resultList = list(uniqueSet)
    resultList.sort()
    return resultList