from typing import List, Any

def filter_integers(input_array: List[Any]) -> List[int]:
    index: int = 0
    result: List[int] = []
    while index < len(input_array):
        current = input_array[index]
        if not isinstance(current, int):
            index += 1
            continue
        result.append(current)
        index += 1
    return result