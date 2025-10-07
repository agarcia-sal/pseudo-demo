from typing import List, Tuple


def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    found_positions: List[Tuple[int, int]] = []
    r_idx: int = 0
    while r_idx < len(two_dimensional_list):
        c_idx: int = 0
        while c_idx < len(two_dimensional_list[r_idx]):
            if two_dimensional_list[r_idx][c_idx] == target_integer:
                found_positions.append((r_idx, c_idx))
            c_idx += 1
        r_idx += 1

    # Sort by column descending, then by row ascending
    found_positions.sort(key=lambda x: x[1], reverse=True)
    found_positions.sort(key=lambda x: x[0])
    return found_positions