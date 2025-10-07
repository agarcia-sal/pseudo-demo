from typing import List

def pluck(array_of_nodes: List[int]) -> List[int]:
    result: List[int] = []

    if not len(array_of_nodes) > 0:
        return result

    filtered_evens: List[int] = []
    pos: int = 0

    while pos < len(array_of_nodes):
        current_element = array_of_nodes[pos]
        if current_element % 2 == 0:
            filtered_evens.append(current_element)
        pos += 1

    if not len(filtered_evens) > 0:
        return result

    min_even_value = filtered_evens[0]
    idx_in_filtered = 0
    scan_pos = 1

    while scan_pos < len(filtered_evens):
        if filtered_evens[scan_pos] < min_even_value:
            min_even_value = filtered_evens[scan_pos]
            idx_in_filtered = scan_pos
        scan_pos += 1

    locate_pos = 0
    found_pos = -1

    while locate_pos < len(array_of_nodes):
        if array_of_nodes[locate_pos] == min_even_value:
            found_pos = locate_pos
            break
        locate_pos += 1

    if found_pos >= 0:
        result = [min_even_value, found_pos]

    return result