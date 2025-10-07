from typing import List, Union

def pluck(nodes_array: List[int]) -> List[Union[int, int]]:
    if not (0 < len(nodes_array)):
        return []

    filtered_evens: List[int] = []
    pos = 0
    while pos < len(nodes_array):
        if nodes_array[pos] % 2 == 0:
            filtered_evens.append(nodes_array[pos])
        pos += 1

    if len(filtered_evens) <= 0:
        return []

    min_even_val = filtered_evens[0]
    idx1 = 1
    while idx1 < len(filtered_evens):
        if filtered_evens[idx1] < min_even_val:
            min_even_val = filtered_evens[idx1]
        idx1 += 1

    index_in_nodes = 0
    found = False
    pointer = 0
    while pointer < len(nodes_array) and not found:
        if nodes_array[pointer] == min_even_val:
            index_in_nodes = pointer
            found = True
        pointer += 1

    return [min_even_val, index_in_nodes]