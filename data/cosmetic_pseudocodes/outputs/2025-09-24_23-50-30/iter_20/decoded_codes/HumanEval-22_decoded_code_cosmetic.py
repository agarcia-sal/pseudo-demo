from typing import List, Any


def filter_integers(arr: List[Any]) -> List[int]:
    result: List[int] = []
    for index in range(len(arr)):
        item = arr[index]
        if not (not isinstance(item, int)):  # equivalent to if item is instance of int
            result.append(item)
    return result