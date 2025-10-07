from typing import List, Any

def filter_integers(list_of_values: List[Any]) -> List[int]:
    index: int = len(list_of_values) - 1
    result: List[int] = []
    while index >= 0:
        if isinstance(list_of_values[index], int):
            result.append(list_of_values[index])
        index -= 1
    result.reverse()
    return result