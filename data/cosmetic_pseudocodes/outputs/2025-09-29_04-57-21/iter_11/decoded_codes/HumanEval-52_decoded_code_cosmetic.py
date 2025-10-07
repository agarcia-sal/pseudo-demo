from typing import Iterable, TypeVar

T = TypeVar('T')

def below_threshold(collection_of_values: Iterable[T], limit: T) -> bool:
    index_tracker = 0
    values_list = list(collection_of_values)  # Ensure indexable in case it's a general iterable
    while index_tracker < len(values_list):
        current_value = values_list[index_tracker]
        if not (current_value < limit):
            return False
        index_tracker += 1
    return True