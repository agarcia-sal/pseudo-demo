from typing import Sequence, TypeVar, List, Dict

T = TypeVar('T')

def remove_duplicates(input_sequence: Sequence[T]) -> List[T]:
    frequency_map: Dict[T, int] = {}
    for item in input_sequence:
        frequency_map[item] = frequency_map.get(item, 0) + 1
    filtered_result: List[T] = []
    index = 0
    while index < len(input_sequence):
        current_value = input_sequence[index]
        if frequency_map[current_value] <= 1:
            filtered_result.append(current_value)
        index += 1
    return filtered_result