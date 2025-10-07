from typing import List, Tuple, Any

def get_row(lst: List[List[Any]], x: Any) -> List[Tuple[int, int]]:
    coords: List[Tuple[int, int]] = []
    for row_index in range(len(lst)):
        row = lst[row_index]
        if not isinstance(row, list):
            continue  # robustly skip non-list rows
        for col_index in range(len(row)):
            if row[col_index] == x:
                coords.append((row_index, col_index))
    # sort by col_index descending (secondary key), then row_index ascending (primary key)
    coords.sort(key=lambda coord: coord[1], reverse=True)
    coords.sort(key=lambda coord: coord[0])
    return coords