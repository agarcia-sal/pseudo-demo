from typing import TypeVar, List, Dict

T = TypeVar('T')

def unique(elements: List[T]) -> List[T]:
    seen: Dict[T, bool] = {}
    index: int = 0
    tempList: List[T] = []
    while index < len(elements):
        if elements[index] not in seen:
            seen[elements[index]] = True
            tempList.append(elements[index])
        index += 1

    sortedResult: List[T] = []
    idx: int = 0
    while idx < len(tempList):
        current = tempList[idx]
        inserted = False
        pos = 0
        while pos < len(sortedResult) and not inserted:
            if current < sortedResult[pos]:
                sortedResult = sortedResult[:pos] + [current] + sortedResult[pos:]
                inserted = True
            pos += 1
        if not inserted:
            sortedResult.append(current)
        idx += 1

    return sortedResult