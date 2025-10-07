from typing import Sequence, List, TypeVar

T = TypeVar('T')

def sort_even(original_sequence: Sequence[T]) -> List[T]:
    primary_elements: List[T] = []
    secondary_elements: List[T] = []
    position_counter: int = 0
    for element in original_sequence:
        if position_counter % 2 == 0:
            primary_elements.append(element)
        else:
            secondary_elements.append(element)
        position_counter += 1

    primary_elements.sort()  # sort ascending

    combined_result: List[T] = []
    index_tracker: int = 0
    while index_tracker < len(secondary_elements):
        combined_result.append(primary_elements[index_tracker])
        combined_result.append(secondary_elements[index_tracker])
        index_tracker += 1

    if len(primary_elements) > len(secondary_elements):
        combined_result.append(primary_elements[-1])

    return combined_result