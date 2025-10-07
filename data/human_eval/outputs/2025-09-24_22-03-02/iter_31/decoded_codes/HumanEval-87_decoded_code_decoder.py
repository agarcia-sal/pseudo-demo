from typing import List, Tuple, Any

def get_row(lst: List[List[Any]], x: Any) -> List[Tuple[int, int]]:
    coords = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == x:
                coords.append((i, j))
    sorted_by_column_desc = []
    for current in coords:
        inserted = False
        for m in range(len(sorted_by_column_desc)):
            if current[1] > sorted_by_column_desc[m][1]:
                sorted_by_column_desc.insert(m, current)
                inserted = True
                break
        if not inserted:
            sorted_by_column_desc.append(current)
    sorted_by_row_asc = []
    for current in sorted_by_column_desc:
        inserted = False
        for q in range(len(sorted_by_row_asc)):
            if current[0] < sorted_by_row_asc[q][0]:
                sorted_by_row_asc.insert(q, current)
                inserted = True
                break
        if not inserted:
            sorted_by_row_asc.append(current)
    return sorted_by_row_asc