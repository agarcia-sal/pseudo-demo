from typing import Any, List

def filter_integers(values: List[Any]) -> List[int]:
    result: List[int] = []
    length_values = len(values)
    index = 0
    while index < length_values:
        x = values[index]
        if type(x) == int:
            result.append(x)
        index += 1
    return result