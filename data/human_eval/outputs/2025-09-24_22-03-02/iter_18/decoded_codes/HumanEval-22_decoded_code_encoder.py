from typing import Any, List

def filter_integers(values: List[Any]) -> List[int]:
    result: List[int] = []
    index = 0
    while index < len(values):
        x = values[index]
        if isinstance(x, int):
            result.append(x)
        index += 1
    return result