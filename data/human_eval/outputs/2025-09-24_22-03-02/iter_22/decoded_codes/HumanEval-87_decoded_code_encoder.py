from typing import List, Tuple

def get_row(lst: List[List[int]], x: int) -> List[Tuple[int, int]]:
    coords = []
    i = 0
    while i < len(lst):
        j = 0
        while j < len(lst[i]):
            if lst[i][j] == x:
                coords.append((i, j))
            j += 1
        i += 1

    temp_sorted_coords = []
    k = 0
    while k < len(coords):
        inserted = False
        m = 0
        while m < len(temp_sorted_coords) and not inserted:
            if coords[k][1] > temp_sorted_coords[m][1]:
                temp_sorted_coords.insert(m, coords[k])
                inserted = True
            m += 1
        if not inserted:
            temp_sorted_coords.append(coords[k])
        k += 1

    final_sorted_coords = []
    p = 0
    while p < len(temp_sorted_coords):
        inserted_final = False
        q = 0
        while q < len(final_sorted_coords) and not inserted_final:
            if temp_sorted_coords[p][0] < final_sorted_coords[q][0]:
                final_sorted_coords.insert(q, temp_sorted_coords[p])
                inserted_final = True
            q += 1
        if not inserted_final:
            final_sorted_coords.append(temp_sorted_coords[p])
        p += 1

    return final_sorted_coords