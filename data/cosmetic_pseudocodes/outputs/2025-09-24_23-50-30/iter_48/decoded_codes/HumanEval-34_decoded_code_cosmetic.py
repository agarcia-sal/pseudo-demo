from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(collection_of_items: Iterable[T]) -> List[T]:
    accumulator: List[T] = []
    processed: set[T] = set()
    index: int = 0
    items = list(collection_of_items)  # To allow indexing

    while index < len(items):
        item = items[index]
        if item not in processed:
            accumulator.append(item)
            processed.add(item)
        index += 1

    result: List[T] = accumulator
    n = len(result)
    for i in range(1, n):
        for j in range(n - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]

    return result