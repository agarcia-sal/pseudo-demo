from typing import List, Tuple

def get_row(lst: List[List[int]], x: int) -> List[Tuple[int, int]]:
    coords = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == x:
                coords.append((i, j))
    coords_sorted_by_column_desc = sorted(coords, key=lambda coord: coord[1], reverse=True)
    coords_sorted_by_row_asc = sorted(coords_sorted_by_column_desc, key=lambda coord: coord[0])
    return coords_sorted_by_row_asc