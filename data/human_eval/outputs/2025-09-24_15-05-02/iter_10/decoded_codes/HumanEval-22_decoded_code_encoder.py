from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    result = []
    for element in values:
        if isinstance(element, int):
            result.append(element)
    return result