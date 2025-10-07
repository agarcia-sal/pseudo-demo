from typing import Any, List

def filter_integers(values: List[Any]) -> List[int]:
    result: List[int] = []
    for index in range(len(values)):
        if type(values[index]) == int:
            result.append(values[index])
    return result