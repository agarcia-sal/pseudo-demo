from typing import List

def is_sorted(list_of_numbers: List[int]) -> bool:
    freq_map = {num: 0 for num in list_of_numbers}
    idx = 0
    while idx < len(list_of_numbers):
        curr_num = list_of_numbers[idx]
        curr_count = freq_map[curr_num]
        updated_count = curr_count + 1
        freq_map[curr_num] = updated_count
        idx += 1

    check_duplicate_excess = False
    iter_idx = 0
    while iter_idx < len(list_of_numbers):
        element_val = list_of_numbers[iter_idx]
        freq_val = freq_map[element_val]
        if freq_val > 2:
            check_duplicate_excess = True
        iter_idx += 1

    if check_duplicate_excess:
        return False

    ascending_flag = True
    pos_idx = 1
    while pos_idx < len(list_of_numbers):
        prior_val = list_of_numbers[pos_idx - 1]
        curr_val = list_of_numbers[pos_idx]
        if not (prior_val <= curr_val):
            ascending_flag = False
        pos_idx += 1

    if ascending_flag:
        return True
    else:
        return False