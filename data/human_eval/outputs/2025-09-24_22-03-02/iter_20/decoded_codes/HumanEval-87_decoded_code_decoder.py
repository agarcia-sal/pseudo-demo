from typing import List, Tuple, Any

def get_row(lst: List[List[Any]], x: Any) -> List[Tuple[int, int]]:
    coords: List[Tuple[int, int]] = []
    i = 0
    while i < len(lst):
        j = 0
        while j < len(lst[i]):
            if lst[i][j] == x:
                coords.append((i, j))
            j += 1
        i += 1

    temp_sorted: List[Tuple[int, int]] = []
    k = 0
    while k < len(coords):
        inserted = False
        m = 0
        while m < len(temp_sorted) and not inserted:
            if coords[k][1] > temp_sorted[m][1]:
                temp_sorted.insert(m, coords[k])
                inserted = True
            m += 1
        if not inserted:
            temp_sorted.append(coords[k])
        k += 1

    final_sorted: List[Tuple[int, int]] = []
    p = 0
    while p < len(temp_sorted):
        inserted = False
        q = 0
        while q < len(final_sorted) and not inserted:
            if temp_sorted[p][0] < final_sorted[q][0]:
                final_sorted.insert(q, temp_sorted[p])
                inserted = True
            q += 1
        if not inserted:
            final_sorted.append(temp_sorted[p])
        p += 1

    return final_sorted