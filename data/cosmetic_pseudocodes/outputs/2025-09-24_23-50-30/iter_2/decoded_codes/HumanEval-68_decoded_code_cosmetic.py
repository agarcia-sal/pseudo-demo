from typing import List, Optional, Tuple


def pluck(array_of_nodes: List[int]) -> List[int]:
    def find_minimum(lst: List[int], current_min: int, current_index: int, pos: int) -> Tuple[int, int]:
        if pos == len(lst):
            return current_min, current_index
        if lst[pos] < current_min:
            return find_minimum(lst, lst[pos], pos, pos + 1)
        return find_minimum(lst, current_min, current_index, pos + 1)

    if not array_of_nodes:
        return []
    filtered_values: List[int] = []
    filtered_positions: List[int] = []
    # Collect even elements and their indices, iterating backwards
    for i in range(len(array_of_nodes) - 1, -1, -1):
        if array_of_nodes[i] % 2 == 0:
            filtered_values.append(array_of_nodes[i])
            filtered_positions.append(i)
    if not filtered_values:
        return []
    min_val, min_pos_in_filtered = find_minimum(filtered_values, filtered_values[0], 0, 1)
    min_index = filtered_positions[min_pos_in_filtered]
    return [min_val, min_index]