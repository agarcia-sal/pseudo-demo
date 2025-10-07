from typing import List, Tuple

def get_row(lst: List[List[int]], x: int) -> List[Tuple[int, int]]:
    coords = []
    i = 0
    len_lst = len(lst)
    while i < len_lst:
        current_row = lst[i]
        j = 0
        len_current_row = len(current_row)
        while j < len_current_row:
            current_element = current_row[j]
            if current_element == x:
                coords.append((i, j))
            j += 1
        i += 1
    coords_sorted_by_column_desc = sorted(coords, key=lambda coord: coord[1], reverse=True)
    coords_sorted_by_row_asc = sorted(coords_sorted_by_column_desc, key=lambda coord: coord[0])
    return coords_sorted_by_row_asc