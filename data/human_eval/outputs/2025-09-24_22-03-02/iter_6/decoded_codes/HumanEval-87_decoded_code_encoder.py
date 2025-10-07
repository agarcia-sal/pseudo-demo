from typing import List, Tuple

def get_row(lst: List[List[int]], x: int) -> List[Tuple[int, int]]:
    coordinates = []
    for row_index in range(len(lst)):
        for column_index in range(len(lst[row_index])):
            if lst[row_index][column_index] == x:
                coordinates.append((row_index, column_index))
    coordinates.sort(key=lambda c: c[1], reverse=True)
    coordinates.sort(key=lambda c: c[0])
    return coordinates