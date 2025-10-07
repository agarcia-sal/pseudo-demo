from typing import List, Tuple, Any

def get_row(lst: List[List[Any]], x: Any) -> List[Tuple[int, int]]:
    coords = []
    i = 0
    while i < len(lst):
        row = lst[i]
        j = 0
        while j < len(row):
            if row[j] == x:
                coords.append((i, j))
            j += 1
        i += 1
    coords_sorted_by_column_desc = []
    index = 0
    while index < len(coords):
        current = coords[index]
        coords_sorted_by_column_desc.append(current)
        index += 1
    coords_sorted_by_column_desc = sorted(coords, key=lambda t: t[1], reverse=True)
    coords_sorted_by_row_asc = sorted(coords_sorted_by_column_desc, key=lambda t: t[0])
    return coords_sorted_by_row_asc