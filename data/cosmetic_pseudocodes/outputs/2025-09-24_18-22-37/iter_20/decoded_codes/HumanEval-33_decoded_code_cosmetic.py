from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_input: List[T]) -> List[T]:
    local_list: List[T] = list(list_input)
    indices_multiple_of_three: List[T] = []
    idx: int = 0
    while idx < len(local_list):
        if idx % 3 == 0:
            indices_multiple_of_three.append(local_list[idx])
        idx += 1

    sorted_subset: List[T] = []
    pos1: int = 0
    while pos1 < len(indices_multiple_of_three):
        min_val: T = indices_multiple_of_three[0]
        min_idx: int = 0
        pos2: int = 1
        while pos2 < len(indices_multiple_of_three):
            if indices_multiple_of_three[pos2] < min_val:
                min_val = indices_multiple_of_three[pos2]
                min_idx = pos2
            pos2 += 1
        temp_val: T = indices_multiple_of_three.pop(min_idx)
        sorted_subset.append(temp_val)
        pos1 += 1

    replacement_pos: int = 0
    iter_index: int = 0
    while iter_index < len(local_list):
        if iter_index % 3 == 0:
            local_list[iter_index] = sorted_subset[replacement_pos]
            replacement_pos += 1
        iter_index += 1

    return local_list