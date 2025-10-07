from typing import List, Any

def filter_integers(list_of_values: List[Any]) -> List[int]:
    selection_result: List[int] = []
    position_tracker: int = 0
    while position_tracker < len(list_of_values):
        candidate = list_of_values[position_tracker]
        if not isinstance(candidate, int):
            position_tracker += 1
            continue
        selection_result.append(candidate)
        position_tracker += 1
    return selection_result