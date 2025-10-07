from typing import Iterable, List, TypeVar

T = TypeVar('T', bound=object)

def unique(collection: Iterable[T]) -> List[T]:
    accumulator: List[T] = []
    checker: dict[T, bool] = {}

    for item in collection:
        if item not in checker:
            accumulator.append(item)
            checker[item] = True

    return sorted(accumulator)