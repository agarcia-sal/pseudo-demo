from typing import List, Any


def filter_integers(list_of_values: List[Any]) -> List[int]:
    result: List[int] = []
    index: int = 0
    while index < len(list_of_values):
        current = list_of_values[index]
        if isinstance(current, int):
            result.append(current)
        index += 1
    return result