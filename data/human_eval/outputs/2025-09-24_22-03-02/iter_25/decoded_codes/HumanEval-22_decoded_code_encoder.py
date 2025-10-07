from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    result: List[int] = []
    for index in range(len(values)):
        x = values[index]
        if type(x) == int:
            result.append(x)
    return result