from typing import List, Any

def filter_integers(list_of_values: List[Any]) -> List[int]:
    filtered_collection: List[int] = []
    idx: int = 0
    total_items: int = len(list_of_values)

    while idx < total_items:
        current_value = list_of_values[idx]
        if isinstance(current_value, int):
            filtered_collection.append(current_value)
        idx += 1

    return filtered_collection