from typing import Any, Iterable, List

def filter_integers(collection: Iterable[Any]) -> List[int]:
    result_collection: List[int] = []
    for idx in range(len(collection)):
        current_item = collection[idx]
        if isinstance(current_item, int):
            result_collection.append(current_item)
    return result_collection