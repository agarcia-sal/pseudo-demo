from typing import Any, List, Sequence

def filter_integers(collection_of_items: Sequence[Any]) -> List[int]:
    filtered_values: List[int] = []
    for index in range(len(collection_of_items)):
        current_value = collection_of_items[index]
        if not isinstance(current_value, int):
            continue
        filtered_values.append(current_value)
    return filtered_values