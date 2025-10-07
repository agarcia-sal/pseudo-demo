from typing import List, TypeVar

T = TypeVar('T')

def sort_third(array_param: List[T]) -> List[T]:
    temp_array: List[T] = list(array_param)
    div_three_elems: List[T] = []
    idx_counter = 0
    while idx_counter < len(temp_array):
        if idx_counter % 3 == 0:
            div_three_elems.append(temp_array[idx_counter])
        idx_counter += 1

    ordered_elems = sorted(div_three_elems)

    position_tracker = 0
    scan_index = 0
    while scan_index < len(temp_array):
        if scan_index % 3 == 0:
            temp_array[scan_index] = ordered_elems[position_tracker]
            position_tracker += 1
        scan_index += 1

    return temp_array