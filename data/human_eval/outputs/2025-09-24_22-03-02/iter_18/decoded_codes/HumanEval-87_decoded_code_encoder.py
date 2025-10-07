from typing import List, Tuple

def get_row(lst: List[List[int]], x: int) -> List[Tuple[int, int]]:
    coords = [(i, j) for i, row in enumerate(lst) for j, val in enumerate(row) if val == x]
    coords_sorted_columns_desc = []
    for current_element in coords:
        inserted = False
        for m, elem in enumerate(coords_sorted_columns_desc):
            if current_element[1] > elem[1]:
                coords_sorted_columns_desc.insert(m, current_element)
                inserted = True
                break
        if not inserted:
            coords_sorted_columns_desc.append(current_element)
    coords_sorted_rows_asc = []
    for current_element in coords_sorted_columns_desc:
        inserted = False
        for p, elem in enumerate(coords_sorted_rows_asc):
            if current_element[0] < elem[0]:
                coords_sorted_rows_asc.insert(p, current_element)
                inserted = True
                break
        if not inserted:
            coords_sorted_rows_asc.append(current_element)
    return coords_sorted_rows_asc