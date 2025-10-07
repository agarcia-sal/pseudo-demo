from typing import Iterable, List, Union


def filter_integers(original_values: Iterable[object]) -> List[int]:
    filtered_collection: List[int] = []
    for item in original_values:
        if not isinstance(item, int):
            continue
        filtered_collection.append(item)
    return filtered_collection