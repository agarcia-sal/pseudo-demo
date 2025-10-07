from typing import List, Any

def filter_integers(list_of_values: List[Any]) -> List[int]:
    filtered_results: List[int] = []
    index: int = 0
    while index < len(list_of_values):
        candidate = list_of_values[index]
        if not isinstance(candidate, int):
            index += 1
            continue
        filtered_results.append(candidate)
        index += 1
    return filtered_results