from typing import List, Tuple, Any

def get_row(lst: List[List[Any]], x: Any) -> List[Tuple[int, int]]:
    coords = []
    i = 0
    while i < len(lst):
        j = 0
        while j < len(lst[i]):
            if lst[i][j] == x:
                coords.append((i, j))
            j += 1
        i += 1

    coords_sorted_by_column_desc = []
    k = 0
    while k < len(coords):
        current = coords[k]
        inserted = False
        l = 0
        while l < len(coords_sorted_by_column_desc) and not inserted:
            if current[1] > coords_sorted_by_column_desc[l][1]:
                coords_sorted_by_column_desc.insert(l, current)
                inserted = True
            l += 1
        if not inserted:
            coords_sorted_by_column_desc.append(current)
        k += 1

    coords_sorted_final = []
    m = 0
    while m < len(coords_sorted_by_column_desc):
        current = coords_sorted_by_column_desc[m]
        inserted = False
        n = 0
        while n < len(coords_sorted_final) and not inserted:
            if current[0] < coords_sorted_final[n][0]:
                coords_sorted_final.insert(n, current)
                inserted = True
            n += 1
        if not inserted:
            coords_sorted_final.append(current)
        m += 1

    return coords_sorted_final