from typing import List, Tuple

def get_row(lst: List[List[int]], x: int) -> List[Tuple[int, int]]:
    if not isinstance(lst, list) or not all(isinstance(row, list) for row in lst):
        raise ValueError("Input lst must be a list of lists")
    if not isinstance(x, int):
        raise ValueError("Input x must be an integer")
    coords: List[Tuple[int, int]] = [
        (i, j)
        for i, row in enumerate(lst)
        for j, val in enumerate(row)
        if val == x
    ]
    # Sort by column descending, then by row ascending
    coords_sorted_desc_col = sorted(coords, key=lambda coord: coord[1], reverse=True)
    coords_sorted = sorted(coords_sorted_desc_col, key=lambda coord: coord[0])
    return coords_sorted