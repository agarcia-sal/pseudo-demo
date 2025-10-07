from typing import List, Tuple, Any

def get_row(lst: List[List[Any]], x: Any) -> List[Tuple[int, int]]:
    coords: List[Tuple[int, int]] = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == x:
                coords.append((i, j))
    coords_sorted_by_col_desc = sorted(coords, key=lambda c: c[1], reverse=True)
    coords_sorted_by_row_asc = sorted(coords_sorted_by_col_desc, key=lambda c: c[0])
    return coords_sorted_by_row_asc