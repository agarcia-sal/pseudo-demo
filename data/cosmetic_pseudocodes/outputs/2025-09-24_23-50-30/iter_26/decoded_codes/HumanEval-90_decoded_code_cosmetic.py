from typing import Iterable, Optional, Union

def next_smallest(collection_numeric: Iterable[Union[int, float]]) -> Optional[Union[int, float]]:
    filtered_collection = []
    for element in collection_numeric:
        if element not in filtered_collection:
            filtered_collection.append(element)
    ordered_collection = sorted(filtered_collection)
    if len(ordered_collection) < 2:
        return None
    return ordered_collection[1]