from typing import Iterable, TypeVar, List

T = TypeVar('T')

def unique(input_sequence: Iterable[T]) -> List[T]:
    temp_storage: List[T] = []
    seen_map: dict[T, bool] = {}
    for element in input_sequence:
        if element not in seen_map:
            temp_storage.append(element)
            seen_map[element] = True
    # sort temp_storage using a simple insertion sort style comparison
    for i in range(len(temp_storage) - 1):
        for j in range(i + 1, len(temp_storage)):
            if temp_storage[j] < temp_storage[i]:
                temp_storage[i], temp_storage[j] = temp_storage[j], temp_storage[i]
    return temp_storage