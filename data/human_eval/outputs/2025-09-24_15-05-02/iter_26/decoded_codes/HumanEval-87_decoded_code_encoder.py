from typing import List, Tuple

def get_row(list_of_lists: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    coordinates: List[Tuple[int, int]] = []
    for row_index, row in enumerate(list_of_lists):
        for column_index, value in enumerate(row):
            if value == target_integer:
                coordinates.append((row_index, column_index))
    # Sort by column_index descending, then by row_index ascending
    coordinates.sort(key=lambda coord: coord[1], reverse=True)
    coordinates.sort(key=lambda coord: coord[0])
    return coordinates