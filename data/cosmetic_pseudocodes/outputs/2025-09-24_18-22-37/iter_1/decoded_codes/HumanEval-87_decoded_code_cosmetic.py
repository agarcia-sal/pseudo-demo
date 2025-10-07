from typing import List, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    coordinates: List[Tuple[int, int]] = []
    for row_idx in range(len(two_dimensional_list)):
        for col_idx in range(len(two_dimensional_list[row_idx])):
            if two_dimensional_list[row_idx][col_idx] == target_integer:
                coordinates.append((row_idx, col_idx))
    coordinates.sort(key=lambda x: (x[0], -x[1]))
    return coordinates