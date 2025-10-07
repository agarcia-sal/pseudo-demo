from typing import List, TypeVar

T = TypeVar('T')

def sort_third(arr_param: List[T]) -> List[T]:
    working_arr = arr_param.copy()
    gather_vals: List[T] = []
    idx_counter = 0
    while idx_counter < len(working_arr):
        if idx_counter % 3 == 0:
            gather_vals.append(working_arr[idx_counter])
        idx_counter += 1

    sorted_gather: List[T] = []
    temp_list = gather_vals
    while temp_list:
        min_val = temp_list[0]
        for i in range(1, len(temp_list)):
            if temp_list[i] < min_val:
                min_val = temp_list[i]

        sorted_gather.append(min_val)
        temp_list = [element for element in temp_list if element != min_val]

    replace_idx = 0
    for pos in range(len(working_arr)):
        if pos % 3 == 0:
            working_arr[pos] = sorted_gather[replace_idx]
            replace_idx += 1

    return working_arr