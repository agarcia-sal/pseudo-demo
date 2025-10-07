from typing import TypeVar, Iterable, List, Dict

T = TypeVar('T')

def unique(container: Iterable[T]) -> List[T]:
    index: int = 0
    accumulator: List[T] = []
    presence: Dict[T, bool] = {}

    container_list = list(container)  # Ensure indexable

    while index < len(container_list):
        item = container_list[index]
        if item not in presence:
            presence[item] = True
            accumulator.append(item)
        index += 1

    sortedResult: List[T] = accumulator[:]
    swapped: bool = True

    while swapped:
        swapped = False
        pos: int = 0
        while pos < len(sortedResult) - 1:
            if not (sortedResult[pos] <= sortedResult[pos + 1]):
                sortedResult[pos], sortedResult[pos + 1] = sortedResult[pos + 1], sortedResult[pos]
                swapped = True
            pos += 1

    return sortedResult