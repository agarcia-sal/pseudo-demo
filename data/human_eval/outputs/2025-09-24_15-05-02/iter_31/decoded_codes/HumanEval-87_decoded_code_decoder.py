from typing import List, Tuple

def get_row(list_of_lists: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    coordinates = [
        (row_idx, col_idx)
        for row_idx, row in enumerate(list_of_lists)
        for col_idx, val in enumerate(row)
        if val == target_integer
    ]
    # Sort by column index descending, then by row index ascending
    coordinates.sort(key=lambda x: x[1], reverse=True)
    coordinates.sort(key=lambda x: x[0])
    return coordinates