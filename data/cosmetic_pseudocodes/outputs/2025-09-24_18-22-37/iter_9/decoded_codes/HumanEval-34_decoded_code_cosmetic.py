from typing import List, TypeVar

T = TypeVar('T', bound=object)

def unique(array_values: List[T]) -> List[T]:
    tempSet = set()
    for idx in range(len(array_values)):
        tempSet.add(array_values[idx])
    tempList = list(tempSet)
    sortedList = sorted(tempList)
    return sortedList