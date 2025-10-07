from typing import List, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    found_positions: List[Tuple[int, int]] = []
    for idx_row in range(len(two_dimensional_list)):
        for idx_col in range(len(two_dimensional_list[idx_row])):
            if two_dimensional_list[idx_row][idx_col] == target_integer:
                found_positions.append((idx_row, idx_col))
    # Sort by column descending, then by row ascending
    found_positions.sort(key=lambda x: x[1], reverse=True)
    found_positions.sort(key=lambda x: x[0])
    return found_positions