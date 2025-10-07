from typing import List, Any

def filter_integers(list_of_values: List[Any]) -> List[int]:
    filtered_result: List[int] = []
    iterator: int = 0

    while iterator < len(list_of_values):
        current_item = list_of_values[iterator]
        if not (type(current_item) != int):
            filtered_result.append(current_item)
        iterator += 1

    return filtered_result