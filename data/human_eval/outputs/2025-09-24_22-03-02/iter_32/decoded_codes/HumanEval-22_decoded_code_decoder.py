from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    result: List[int] = []
    length_of_values = len(values)
    index = 0
    while index < length_of_values:
        x = values[index]
        if isinstance(x, int):
            result.append(x)
        index += 1
    return result