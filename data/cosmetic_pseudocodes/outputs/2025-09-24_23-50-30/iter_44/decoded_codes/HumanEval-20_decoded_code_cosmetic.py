from typing import List, Optional, Tuple


def find_closest_elements(array_of_values: List[int]) -> Optional[Tuple[int, int]]:
    best_match: Optional[Tuple[int, int]] = None
    smallest_gap: Optional[int] = None

    def inner_loop(pos1: int, val1: int, pos2: int) -> None:
        nonlocal best_match, smallest_gap
        if pos2 >= len(array_of_values):
            return
        current_val = array_of_values[pos2]
        if pos1 != pos2:
            current_dist = abs(val1 - current_val)
            if smallest_gap is None or current_dist < smallest_gap:
                smallest_gap = current_dist
                pair_list = [val1, current_val]
                pair_list.sort()
                best_match = (pair_list[0], pair_list[1])
        inner_loop(pos1, val1, pos2 + 1)

    def outer_loop(pos: int) -> None:
        if pos >= len(array_of_values):
            return
        inner_loop(pos, array_of_values[pos], 0)
        outer_loop(pos + 1)

    outer_loop(0)
    return best_match