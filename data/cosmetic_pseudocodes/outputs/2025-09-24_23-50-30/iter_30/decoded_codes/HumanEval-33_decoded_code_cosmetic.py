from typing import List, Sequence, TypeVar

T = TypeVar('T')

def sort_third(array_data: Sequence[T]) -> List[T]:
    buffer_array: List[T] = list(array_data)
    extracted_elements: List[T] = []
    idx_counter = 0
    while idx_counter < len(buffer_array):
        if idx_counter % 3 == 0:
            extracted_elements.append(buffer_array[idx_counter])
        idx_counter += 1

    ordered_elements = sorted(extracted_elements)

    place_index = 0
    position_tracker = 0
    while position_tracker < len(buffer_array):
        if position_tracker % 3 == 0:
            buffer_array[position_tracker] = ordered_elements[place_index]
            place_index += 1
        position_tracker += 1

    return buffer_array