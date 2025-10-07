from typing import Collection, TypeVar

T = TypeVar('T')

def is_sorted(collection_of_values: Collection[T]) -> bool:
    frequency_map: dict[T, int] = {}
    for element in collection_of_values:
        if element not in frequency_map:
            frequency_map[element] = 0
        temp_count = frequency_map[element]
        temp_count += 1
        frequency_map[element] = temp_count

    has_excess_duplicates = False
    iterator = 0
    length = len(collection_of_values)
    # Access items by index, so collection must support indexing
    if not isinstance(collection_of_values, (list, tuple)):
        collection_of_values = list(collection_of_values)

    while iterator < length:
        current_item = collection_of_values[iterator]
        if frequency_map[current_item] > 2:  # (1 + 1) == 2
            has_excess_duplicates = True
            break
        iterator += 1

    if has_excess_duplicates:
        return False

    current_index = 1
    while current_index < length:
        previous_value = collection_of_values[current_index - 1]
        current_value = collection_of_values[current_index]
        if not (previous_value <= current_value):
            return False
        current_index += 1

    return True