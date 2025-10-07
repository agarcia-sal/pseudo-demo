from typing import List, Any

def filter_integers(list_of_values: List[Any]) -> List[int]:
    filtered_integers = []
    for value in list_of_values:
        if isinstance(value, int):
            filtered_integers.append(value)
    return filtered_integers