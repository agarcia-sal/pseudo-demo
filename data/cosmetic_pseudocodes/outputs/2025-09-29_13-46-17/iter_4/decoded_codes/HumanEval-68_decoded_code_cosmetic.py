from typing import List, Tuple


def pluck(array_of_nodes: List[int]) -> List[int]:
    def find_even_values(index: int, collected: List[int]) -> List[int]:
        if index == len(array_of_nodes):
            return collected
        current_element = array_of_nodes[index]
        new_collected = collected + [current_element] if current_element % 2 == 0 else collected
        return find_even_values(index + 1, new_collected)

    even_set = find_even_values(0, [])
    if not even_set:
        return []

    def find_minimum_value(
        list_values: List[int], idx: int, current_min: int, current_min_index: int
    ) -> Tuple[int, int]:
        if idx == len(list_values):
            return current_min, current_min_index
        value_at_idx = list_values[idx]
        if value_at_idx < current_min:
            return find_minimum_value(list_values, idx + 1, value_at_idx, idx)
        return find_minimum_value(list_values, idx + 1, current_min, current_min_index)

    min_even_val, min_index_in_even = find_minimum_value(even_set, 0, even_set[0], 0)

    def find_index_in_array(target: int, index: int) -> int:
        if index == len(array_of_nodes):
            return -1
        if array_of_nodes[index] == target:
            return index
        return find_index_in_array(target, index + 1)

    index_in_original = find_index_in_array(min_even_val, 0)

    return [min_even_val, index_in_original]