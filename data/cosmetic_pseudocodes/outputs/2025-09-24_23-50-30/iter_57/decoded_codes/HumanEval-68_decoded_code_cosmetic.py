from typing import List, Tuple


def pluck(collection: List[int]) -> List[int]:
    def find_minimum_and_index(
        items: List[int], idx: int, min_val: int, min_pos: int
    ) -> Tuple[int, int]:
        if idx >= len(items):
            return min_val, min_pos
        current_element = items[idx]
        if current_element < min_val:
            return find_minimum_and_index(items, idx + 1, current_element, idx)
        return find_minimum_and_index(items, idx + 1, min_val, min_pos)

    filtered: List[int] = []
    pointer = 0
    while pointer < len(collection):
        candidate = collection[pointer]
        if candidate % 2 == 0:
            filtered.append(candidate)
        pointer += 1

    if not filtered:
        return []

    min_even_value, min_even_index = find_minimum_and_index(filtered, 1, filtered[0], 0)

    actual_index = 0
    search_pos = 0
    while search_pos < len(collection):
        if collection[search_pos] == min_even_value:
            actual_index = search_pos
            break
        search_pos += 1

    return [min_even_value, actual_index]