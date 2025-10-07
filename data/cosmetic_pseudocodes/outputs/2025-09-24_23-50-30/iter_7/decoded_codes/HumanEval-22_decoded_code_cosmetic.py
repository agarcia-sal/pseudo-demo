from typing import List, Any

def filter_integers(list_of_values: List[Any]) -> List[int]:
    filtered_values: List[int] = []
    index_counter: int = 0

    while index_counter < len(list_of_values):
        current_element = list_of_values[index_counter]
        if not isinstance(current_element, int):
            index_counter += 1
            continue
        filtered_values.append(current_element)
        index_counter += 1

    return filtered_values