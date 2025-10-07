from typing import List, Tuple

def get_row(list_of_lists: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    coordinates: List[Tuple[int, int]] = []
    for row_index in range(len(list_of_lists)):
        for column_index in range(len(list_of_lists[row_index])):
            if list_of_lists[row_index][column_index] == target_integer:
                coordinates.append((row_index, column_index))
    # Sort by column index descending
    coordinates.sort(key=lambda x: x[1], reverse=True)
    # Then sort by row index ascending
    coordinates.sort(key=lambda x: x[0])
    return coordinates