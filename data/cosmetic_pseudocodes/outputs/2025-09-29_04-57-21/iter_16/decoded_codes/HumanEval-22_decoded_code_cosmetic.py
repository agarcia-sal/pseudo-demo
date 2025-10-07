from typing import Any, List

def filter_integers(list_of_values: List[Any]) -> List[int]:
    result: List[int] = []
    i: int = 0
    length: int = len(list_of_values)
    while i < length:
        current = list_of_values[i]
        if not isinstance(current, int):
            i += 1
            continue
        result.append(current)
        i += 1
    return result