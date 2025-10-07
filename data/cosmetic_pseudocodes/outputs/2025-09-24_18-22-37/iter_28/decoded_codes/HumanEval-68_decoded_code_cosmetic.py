from typing import List

def pluck(container_of_nodes: List[int]) -> List[int]:
    finished_flag: bool = False
    filtered_evens: List[int] = []
    output_result: List[int] = []
    current_idx: int = 0

    while not finished_flag:
        if current_idx >= len(container_of_nodes):
            finished_flag = True
        else:
            current_element = container_of_nodes[current_idx]
            if current_element % 2 == 0:
                filtered_evens.append(current_element)
            current_idx += 1

    if len(container_of_nodes) == 0:
        return []

    if len(filtered_evens) == 0:
        return []

    min_even_val: int = filtered_evens[0]
    iter_var: int = 1

    while iter_var < len(filtered_evens):
        candidate_val = filtered_evens[iter_var]
        if candidate_val < min_even_val:
            min_even_val = candidate_val
        iter_var += 1

    search_pos: int = 0
    found_flag: bool = False

    while not found_flag and search_pos < len(container_of_nodes):
        possible_match = container_of_nodes[search_pos]
        if possible_match == min_even_val:
            found_flag = True
        else:
            search_pos += 1

    output_result.append(min_even_val)
    output_result.append(search_pos)

    return output_result