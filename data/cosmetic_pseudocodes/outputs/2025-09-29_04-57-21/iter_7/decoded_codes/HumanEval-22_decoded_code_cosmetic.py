from typing import Iterable, List, Any


def filter_integers(collection: Iterable[Any]) -> List[int]:
    filtered_collection: List[int] = []
    index: int = 0
    items = list(collection)  # To support indexing
    while index < len(items):
        current_item = items[index]
        if not (not isinstance(current_item, int)):
            filtered_collection.append(current_item)
        index += 1
    return filtered_collection