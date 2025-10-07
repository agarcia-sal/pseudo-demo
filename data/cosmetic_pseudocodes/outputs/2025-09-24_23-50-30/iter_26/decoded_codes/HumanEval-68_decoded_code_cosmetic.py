from typing import List, Tuple, Optional


def pluck(collection_of_items: List[int]) -> List[int]:
    if len(collection_of_items) == 0:
        return []

    filtered_items: List[int] = [item for item in collection_of_items if item % 2 == 0]
    if not filtered_items:
        return []

    def find_minimum(list_values: List[int], current_min: int, current_pos: int, index_acc: int) -> Tuple[int, int]:
        if index_acc == len(list_values):
            return current_min, current_pos
        if list_values[index_acc] < current_min:
            return find_minimum(list_values, list_values[index_acc], index_acc, index_acc + 1)
        return find_minimum(list_values, current_min, current_pos, index_acc + 1)

    minimum_value, minimum_index_in_filtered = find_minimum(filtered_items, filtered_items[0], 0, 1)

    def find_index(original_list: List[int], target_value: int, current_index: int) -> int:
        if current_index == len(original_list):
            return -1
        if original_list[current_index] == target_value:
            return current_index
        return find_index(original_list, target_value, current_index + 1)

    position_in_original = find_index(collection_of_items, minimum_value, 0)

    return [minimum_value, position_in_original]