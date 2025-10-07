from typing import List, Any

def filter_integers(list_of_values: List[Any]) -> List[int]:
    filtered_values: List[int] = []
    index: int = 0
    while index < len(list_of_values):
        current_element = list_of_values[index]
        if isinstance(current_element, int):
            filtered_values.append(current_element)
        index += 1
    return filtered_values