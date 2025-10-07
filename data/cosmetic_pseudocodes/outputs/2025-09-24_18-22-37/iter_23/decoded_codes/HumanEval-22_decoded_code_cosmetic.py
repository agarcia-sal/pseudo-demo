from typing import Iterable, List, Union

def filter_integers(values_collection: Iterable[object]) -> List[int]:
    filtered_collection: List[int] = []
    position = 0
    values_list = list(values_collection)
    while position < len(values_list):
        candidate = values_list[position]
        if isinstance(candidate, int):
            filtered_collection.append(candidate)
        position += 1
    return filtered_collection