from typing import List

def pluck(list_of_nodes: List[int]) -> List[int]:
    result_list: List[int] = []
    temp_evens: List[int] = []

    count_nodes = len(list_of_nodes)
    if count_nodes <= 0:
        return result_list

    idx = 0
    while idx < count_nodes:
        current_val = list_of_nodes[idx]
        is_even_flag = (current_val % 2) == 0
        if is_even_flag:
            temp_evens.append(current_val)
        idx += 1

    if len(temp_evens) == 0:
        return result_list

    min_even_val = temp_evens[0]
    temp_idx = 1
    while temp_idx < len(temp_evens):
        if temp_evens[temp_idx] < min_even_val:
            min_even_val = temp_evens[temp_idx]
        temp_idx += 1

    found_min_index = 0
    search_idx = 0
    while search_idx < count_nodes:
        candidate_val = list_of_nodes[search_idx]
        if candidate_val == min_even_val:
            found_min_index = search_idx
            break
        search_idx += 1

    result_list = [min_even_val, found_min_index]
    return result_list