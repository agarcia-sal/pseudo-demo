from typing import List, TypeVar

T = TypeVar('T')

def is_sorted(arr: List[T]) -> bool:
    frequency_map: dict[T, int] = {element: 0 for element in arr}
    for element in arr:
        frequency_map[element] += 1

    for element in arr:
        if frequency_map[element] > 2:
            return False

    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return False

    return True