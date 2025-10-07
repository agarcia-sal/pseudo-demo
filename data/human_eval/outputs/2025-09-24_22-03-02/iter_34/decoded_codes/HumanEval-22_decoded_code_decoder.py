from typing import Any, List

def filter_integers(values: List[Any]) -> List[int]:
    result: List[int] = []
    index = 0
    while index < len(values):
        element = values[index]
        if type(element) == int:
            result.append(element)
        index += 1
    return result