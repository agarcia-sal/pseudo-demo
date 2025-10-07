from typing import List

def pluck(list_of_nodes: List[int]) -> List[int]:
    result_list: List[int] = []
    has_elements: int = len(list_of_nodes)
    if has_elements == 0:
        return result_list

    filtered_evens: List[int] = [candidate for candidate in list_of_nodes if candidate % 2 == 0]
    count_evens: int = len(filtered_evens)
    if count_evens == 0:
        return result_list

    minimum_even: int = filtered_evens[0]
    for i in range(1, count_evens):
        current_element: int = filtered_evens[i]
        if current_element < minimum_even:
            minimum_even = current_element

    minimum_even_pos: int = 0
    for j in range(has_elements):
        if list_of_nodes[j] == minimum_even:
            minimum_even_pos = j
            break

    result_list = [minimum_even, minimum_even_pos]
    return result_list