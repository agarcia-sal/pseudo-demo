from typing import Iterable, TypeVar

T = TypeVar('T')

def is_sorted(collection_of_values: Iterable[T]) -> bool:
    frequency_map: dict[T, int] = {}
    values = list(collection_of_values)
    for val in values:
        frequency_map[val] = frequency_map.get(val, 0) + 1
    for count_value in frequency_map.values():
        if count_value > 2:
            return False
    for i in range(1, len(values)):
        if not (values[i - 1] <= values[i]):
            return False
    return True