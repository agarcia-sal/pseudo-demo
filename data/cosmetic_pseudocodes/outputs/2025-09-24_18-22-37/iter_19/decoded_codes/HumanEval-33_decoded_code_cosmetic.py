from typing import List

def sort_third(list_input: List[int]) -> List[int]:
    temp_list: List[int] = list_input.copy()
    extract_indices: List[int] = []
    idx_counter: int = 0

    while idx_counter < len(temp_list):
        idx_holder = idx_counter
        if idx_holder % 3 == 0:
            extract_indices.append(temp_list[idx_holder])
        idx_counter += 1

    sorted_subset: List[int] = sorted(extract_indices)

    idx_counter = 0
    replace_pos: int = 0

    while idx_counter < len(temp_list):
        if idx_counter % 3 == 0:
            temp_list[idx_counter] = sorted_subset[replace_pos]
            replace_pos += 1
        idx_counter += 1

    return temp_list