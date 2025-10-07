from typing import List, Any

def filter_integers(list_of_values: List[Any]) -> List[int]:
    filtered_elements: List[int] = []
    for value in list_of_values:
        if isinstance(value, int):
            filtered_elements.append(value)
    return filtered_elements