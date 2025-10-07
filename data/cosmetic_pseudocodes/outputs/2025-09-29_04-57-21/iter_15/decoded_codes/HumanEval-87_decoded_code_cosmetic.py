from typing import List, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    found_positions: List[Tuple[int, int]] = []
    outer_idx = 0
    while outer_idx < len(two_dimensional_list):
        inner_idx = 0
        while inner_idx < len(two_dimensional_list[outer_idx]):
            if two_dimensional_list[outer_idx][inner_idx] == target_integer:
                found_positions.append((outer_idx, inner_idx))
            inner_idx += 1
        outer_idx += 1

    found_positions.sort(key=lambda pos: -pos[1])  # sort descending by inner_idx
    found_positions.sort(key=lambda pos: pos[0])   # sort ascending by outer_idx

    return found_positions