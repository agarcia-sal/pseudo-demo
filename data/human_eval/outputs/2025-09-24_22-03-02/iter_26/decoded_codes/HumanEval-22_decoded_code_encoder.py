from typing import Any, List

def filter_integers(values: List[Any]) -> List[int]:
    result: List[int] = []
    for x in values:
        if isinstance(x, int):
            result.append(x)
    return result