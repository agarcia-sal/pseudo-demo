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
        current_element = coords[k]
        inserted = False
        m = 0
        while m < len(temp_sorted_coords):
            if current_element[1] > temp_sorted_coords[m][1]:
                temp_sorted_coords.insert(m, current_element)
                inserted = True
                break
            m += 1
        if not inserted:
            temp_sorted_coords.append(current_element)
        k += 1

    final_sorted_coords: List[Tuple[int, int]] = []
    n = 0
    while n < len(temp_sorted_coords):
        current_element = temp_sorted_coords[n]
        inserted = False
        p = 0
        while p < len(final_sorted_coords):
            if current_element[0] < final_sorted_coords[p][0]:
                final_sorted_coords.insert(p, current_element)
                inserted = True
                break
            p += 1
        if not inserted:
            final_sorted_coords.append(current_element)
        n += 1

    return final_sorted_coords