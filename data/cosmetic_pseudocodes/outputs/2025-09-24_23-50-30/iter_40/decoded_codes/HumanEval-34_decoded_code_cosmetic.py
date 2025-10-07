from typing import Iterable, List, TypeVar

T = TypeVar('T', bound=object)

def unique(collection: Iterable[T]) -> List[T]:
    tempSet = set(collection)
    resultList = list(tempSet)
    resultList.sort()
    return resultList