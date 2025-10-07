from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    result: List[int] = []
    for x in values:
        if type(x) == int:
            result.append(x)
    return result