from typing import List, Optional, Tuple

def find_closest_elements(array_of_values: List[int]) -> Optional[Tuple[int, int]]:
    selected_pair: Optional[Tuple[int, int]] = None
    smallest_gap: Optional[int] = None

    def traverse_outer(pos_outer: int) -> None:
        if pos_outer == len(array_of_values):
            return
        traverse_inner(pos_outer, 0)
        traverse_outer(pos_outer + 1)

    def traverse_inner(pos_outer: int, pos_inner: int) -> None:
        nonlocal selected_pair, smallest_gap
        if pos_inner == len(array_of_values):
            return
        if pos_outer != pos_inner:
            diff = array_of_values[pos_outer] - array_of_values[pos_inner]
            abs_diff = diff if diff >= 0 else -diff
            if smallest_gap is None:
                smallest_gap = abs_diff
                pair = (array_of_values[pos_outer], array_of_values[pos_inner])
                selected_pair = (pair[0], pair[1]) if pair[0] <= pair[1] else (pair[1], pair[0])
            elif abs_diff < smallest_gap:
                smallest_gap = abs_diff
                pair = (array_of_values[pos_outer], array_of_values[pos_inner])
                selected_pair = (pair[0], pair[1]) if pair[0] <= pair[1] else (pair[1], pair[0])
        traverse_inner(pos_outer, pos_inner + 1)

    traverse_outer(0)
    return selected_pair