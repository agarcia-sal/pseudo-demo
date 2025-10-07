from typing import List, Tuple, Optional


def pluck(array_of_nodes: List[int]) -> List[int]:
    def find_even_elements(lst: List[int], pos: int, acc: List[int]) -> List[int]:
        if pos == len(lst):
            return acc
        if lst[pos] % 2 == 0:
            return find_even_elements(lst, pos + 1, acc + [lst[pos]])
        return find_even_elements(lst, pos + 1, acc)

    evens = find_even_elements(array_of_nodes, 0, [])

    if not evens:
        return []

    def min_value(values: List[int], idx: int, current_min: int, current_min_idx: int) -> Tuple[int, int]:
        if idx == len(values):
            return current_min, current_min_idx
        if values[idx] < current_min:
            return min_value(values, idx + 1, values[idx], idx)
        return min_value(values, idx + 1, current_min, current_min_idx)

    min_even, _ = min_value(evens, 0, evens[0], 0)

    def find_index(lst: List[int], val: int, i: int) -> int:
        if i == len(lst):
            return -1
        if lst[i] == val:
            return i
        return find_index(lst, val, i + 1)

    min_even_position = find_index(array_of_nodes, min_even, 0)

    return [min_even, min_even_position]