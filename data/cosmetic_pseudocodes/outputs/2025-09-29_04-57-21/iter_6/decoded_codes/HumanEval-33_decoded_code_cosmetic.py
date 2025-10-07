from typing import List

def sort_third(list_input: List[int]) -> List[int]:
    duplicated_list: List[int] = list_input[:]  # duplicate the input list

    filtered_positions: List[int] = []
    filtered_elements: List[int] = []
    position_counter: int = 0
    while position_counter < len(duplicated_list):
        if position_counter % 3 == 0:
            filtered_positions.append(position_counter)
            filtered_elements.append(duplicated_list[position_counter])
        position_counter += 1

    sorted_filtered: List[int] = sorted(filtered_elements)

    idx: int = 0
    for pos in filtered_positions:
        duplicated_list[pos] = sorted_filtered[idx]
        idx += 1

    return duplicated_list