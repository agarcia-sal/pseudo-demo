from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_input: List[T]) -> List[T]:
    duplicate_list: List[T] = list_input[:]
    filtered_elements: List[T] = []
    idx_counter: int = 0
    while idx_counter < len(duplicate_list):
        if idx_counter % 3 == 0:
            filtered_elements.append(duplicate_list[idx_counter])
        idx_counter += 1

    ordered_subset: List[T] = filtered_elements
    ordered_subset.sort()

    replace_pointer: int = 0
    position_tracker: int = 0
    while position_tracker < len(duplicate_list):
        if position_tracker % 3 == 0:
            duplicate_list[position_tracker] = ordered_subset[replace_pointer]
            replace_pointer += 1
        position_tracker += 1

    return duplicate_list