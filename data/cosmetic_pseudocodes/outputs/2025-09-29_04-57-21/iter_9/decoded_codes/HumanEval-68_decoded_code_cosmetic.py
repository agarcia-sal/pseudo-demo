from typing import List, Union

def pluck(array_of_nodes: List[int]) -> List[Union[int, int]]:
    result_list: List[Union[int, int]] = []

    if not array_of_nodes:
        return result_list

    filtered_evens: List[int] = []
    idx: int = 0

    while idx < len(array_of_nodes):
        current_num: int = array_of_nodes[idx]
        if current_num % 2 == 0:
            filtered_evens.append(current_num)
        idx += 1

    if not filtered_evens:
        return result_list

    minimal_even: int = filtered_evens[0]
    for element in filtered_evens:
        if element < minimal_even:
            minimal_even = element

    position_of_minimal: int = 0
    search_index: int = 0

    while search_index < len(array_of_nodes):
        if array_of_nodes[search_index] == minimal_even:
            position_of_minimal = search_index
            break
        search_index += 1

    return [minimal_even, position_of_minimal]