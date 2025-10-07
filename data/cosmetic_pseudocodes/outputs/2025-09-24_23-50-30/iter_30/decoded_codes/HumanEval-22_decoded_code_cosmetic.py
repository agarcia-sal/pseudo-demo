from typing import Any, Iterable, List


def filter_integers(collection_of_items: Iterable[Any]) -> List[int]:
    accumulator: List[int] = []
    index: int = 0
    items = list(collection_of_items)  # ensure indexing
    length = len(items)
    while index < length:
        if isinstance(items[index], int):
            accumulator.append(items[index])
        index += 1
    return accumulator