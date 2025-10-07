from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    result = []
    for x in values:
        if type(x) is int:
            result.append(x)
    return result