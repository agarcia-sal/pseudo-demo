from typing import List, Tuple

def get_row(lst: List[List[int]], x: int) -> List[Tuple[int, int]]:
    coords: List[Tuple[int, int]] = []
    for row_index in range(len(lst)):
        for column_index in range(len(lst[row_index])):
            if lst[row_index][column_index] == x:
                coords.append((row_index, column_index))
    coords.sort(key=lambda coord: coord[1], reverse=True)
    coords.sort(key=lambda coord: coord[0])
    return coords