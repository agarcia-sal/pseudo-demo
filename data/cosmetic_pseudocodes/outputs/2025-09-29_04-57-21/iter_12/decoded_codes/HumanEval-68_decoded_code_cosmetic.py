from typing import List, Union

def pluck(array_of_nodes: List[int]) -> List[Union[int, int]]:
    total_count: int = len(array_of_nodes)
    if not (total_count > 0):
        return []

    extracted_evens: List[int] = []
    position: int = 0

    while position < total_count:
        current_item: int = array_of_nodes[position]
        if (current_item % 2) == 0:
            extracted_evens.append(current_item)
        position += 1

    if not (len(extracted_evens) > 0):
        return []

    min_even_val: int = extracted_evens[0]
    scan_index: int = 1

    while scan_index < len(extracted_evens):
        if extracted_evens[scan_index] < min_even_val:
            min_even_val = extracted_evens[scan_index]
        scan_index += 1

    final_index: int = 0
    while array_of_nodes[final_index] != min_even_val:
        final_index += 1

    return [min_even_val, final_index]