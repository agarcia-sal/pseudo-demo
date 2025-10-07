from typing import Any, List

def filter_integers(values: List[Any]) -> List[int]:
    result: List[int] = []
    index = 0
    length = len(values)
    while index < length:
        current_element = values[index]
        if isinstance(current_element, int):
            result.append(current_element)
        index += 1
    return result