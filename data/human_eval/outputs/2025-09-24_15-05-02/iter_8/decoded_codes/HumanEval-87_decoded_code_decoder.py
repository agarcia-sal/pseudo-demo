from typing import List, Tuple, TypeVar

T = TypeVar('T')

def get_row(lst: List[List[T]], x: T) -> List[Tuple[int, int]]:
    coords: List[Tuple[int, int]] = []
    for i, row in enumerate(lst):
        for j, value in enumerate(row):
            if value == x:
                coords.append((i, j))
    coords_sorted_columns_desc = sorted(coords, key=lambda c: c[1], reverse=True)
    coords_sorted_rows_asc = sorted(coords_sorted_columns_desc, key=lambda c: c[0])
    return coords_sorted_rows_asc