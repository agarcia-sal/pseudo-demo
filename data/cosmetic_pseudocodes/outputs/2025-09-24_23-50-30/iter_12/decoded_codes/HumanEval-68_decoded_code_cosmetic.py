from typing import List, Tuple

def pluck(collection_of_items: List[int]) -> List[int]:
    def find_minimum_index_and_value(items: List[int]) -> Tuple[int, int]:
        pos = 0
        val = items[0]
        for idx in range(1, len(items)):
            if items[idx] < val:
                val = items[idx]
                pos = idx
        return pos, val

    if not collection_of_items:
        return []

    filtered_set = [item for item in collection_of_items if item % 2 == 0]

    if not filtered_set:
        return []

    min_index_filtered, min_value_filtered = find_minimum_index_and_value(filtered_set)

    original_index = 0
    while original_index < len(collection_of_items) and collection_of_items[original_index] != min_value_filtered:
        original_index += 1

    return [min_value_filtered, original_index]