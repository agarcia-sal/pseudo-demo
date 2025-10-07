from typing import List


def sort_third(list_input: List[int]) -> List[int]:
    working_copy: List[int] = list_input.copy()
    filtered_elements: List[int] = []
    position_counter: int = 0

    while position_counter < len(working_copy):
        if position_counter % 3 == 0:
            filtered_elements.append(working_copy[position_counter])
        position_counter += 1

    sorted_elements: List[int] = sorted(filtered_elements)

    idx: int = 0
    elements_iter = iter(working_copy)

    for element in elements_iter:
        current_index = working_copy.index(element)  # index of current element in working_copy
        if current_index % 3 == 0:
            working_copy[current_index] = sorted_elements[idx]
            idx += 1

    return working_copy