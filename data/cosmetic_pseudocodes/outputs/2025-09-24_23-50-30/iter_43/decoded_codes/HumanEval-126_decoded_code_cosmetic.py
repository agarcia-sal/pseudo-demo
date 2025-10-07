from typing import List, Dict, TypeVar

T = TypeVar('T', bound=object)

def is_sorted(array_values: List[T]) -> bool:
    frequency_map: Dict[T, int] = {key: 0 for key in array_values}
    index_pointer = 0
    while index_pointer < len(array_values):
        current_item = array_values[index_pointer]
        frequency_map[current_item] += 1
        index_pointer += 1

    violation_found = False
    key_iterator = list(frequency_map.keys())
    key_index = 0
    while key_index < len(key_iterator) and not violation_found:
        current_key = key_iterator[key_index]
        if frequency_map[current_key] > 2:
            violation_found = True
        key_index += 1

    if violation_found:
        return False

    cursor = 1
    while cursor < len(array_values):
        if not (array_values[cursor - 1] <= array_values[cursor]):
            return False
        cursor += 1

    return True