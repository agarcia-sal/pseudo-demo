from typing import List, Tuple

def get_row(lst: List[List[int]], x: int) -> List[Tuple[int, int]]:
    coords: List[Tuple[int, int]] = []
    i = 0
    while i < len(lst):
        j = 0
        while j < len(lst[i]):
            if lst[i][j] == x:
                coords.append((i, j))
            j += 1
        i += 1

    temp_sorted_coords: List[Tuple[int, int]] = []
    k = 0
    while k < len(coords):
        current_tuple = coords[k]
        inserted = False
        m = 0
        while m < len(temp_sorted_coords) and not inserted:
            if current_tuple[1] > temp_sorted_coords[m][1]:
                temp_sorted_coords.insert(m, current_tuple)
                inserted = True
            m += 1
        if not inserted:
            temp_sorted_coords.append(current_tuple)
        k += 1

    final_sorted_coords: List[Tuple[int, int]] = []
    p = 0
    while p < len(temp_sorted_coords):
        current_tuple = temp_sorted_coords[p]
        inserted = False
        q = 0
        while q < len(final_sorted_coords) and not inserted:
            if current_tuple[0] < final_sorted_coords[q][0]:
                final_sorted_coords.insert(q, current_tuple)
                inserted = True
            q += 1
        if not inserted:
            final_sorted_coords.append(current_tuple)
        p += 1

    return final_sorted_coords