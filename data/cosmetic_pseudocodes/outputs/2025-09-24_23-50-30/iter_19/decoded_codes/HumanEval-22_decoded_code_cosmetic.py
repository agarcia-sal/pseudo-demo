from typing import Iterable, List, Union

def filter_integers(collection: Iterable[object]) -> List[int]:
    filtered_results: List[int] = []
    for value in collection:
        if not isinstance(value, int):
            continue
        filtered_results.append(value)
    return filtered_results