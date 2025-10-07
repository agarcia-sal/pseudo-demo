from typing import List, Tuple

def pluck(array_of_nodes: List[int]) -> List[int]:
    def recursive_find_minimum(items: List[int], current_min: int, current_min_idx: int, pos: int) -> Tuple[int, int]:
        if pos >= len(items):
            return current_min, current_min_idx
        if items[pos] < current_min:
            return recursive_find_minimum(items, items[pos], pos, pos + 1)
        return recursive_find_minimum(items, current_min, current_min_idx, pos + 1)

    if not array_of_nodes:
        return []

    def extract_even(elements: List[int], idx: int, acc: List[int]) -> List[int]:
        if idx == len(elements):
            return acc
        if elements[idx] % 2 == 0:
            return extract_even(elements, idx + 1, acc + [elements[idx]])
        return extract_even(elements, idx + 1, acc)

    even_vals = extract_even(array_of_nodes, 0, [])

    if not even_vals:
        return []

    min_val, _ = recursive_find_minimum(even_vals, even_vals[0], 0, 1)

    def find_original_index(arr: List[int], val: int, pos: int) -> int:
        if pos >= len(arr):
            return -1
        if arr[pos] == val:
            return pos
        return find_original_index(arr, val, pos + 1)

    original_index = find_original_index(array_of_nodes, min_val, 0)

    return [min_val, original_index]