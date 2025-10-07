from typing import Any, List

def filter_integers(values: List[Any]) -> List[int]:
    result: List[int] = []
    for element in values:
        if isinstance(element, int):
            result.append(element)
    return result