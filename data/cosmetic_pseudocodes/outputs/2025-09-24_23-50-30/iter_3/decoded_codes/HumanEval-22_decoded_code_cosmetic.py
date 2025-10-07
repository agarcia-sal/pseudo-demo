from typing import Iterable, List, Union


def filter_integers(values_collection: Iterable[object]) -> List[int]:
    filtered_values: List[int] = []
    for index in range(1, len(values_collection) + 1):
        current_value = values_collection[index - 1]  # zero-based indexing in Python
        if isinstance(current_value, int):
            filtered_values.append(current_value)
    return filtered_values