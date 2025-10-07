from typing import List, Tuple

def get_row(list_of_lists: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    coordinate_list: List[Tuple[int, int]] = []
    for row_index in range(len(list_of_lists)):
        for column_index in range(len(list_of_lists[row_index])):
            if list_of_lists[row_index][column_index] == target_integer:
                coordinate_list.append((row_index, column_index))
    # Sort by column_index descending
    coordinate_list.sort(key=lambda x: x[1], reverse=True)
    # Sort by row_index ascending (stable sort preserves previous order for same row_index)
    coordinate_list.sort(key=lambda x: x[0])
    return coordinate_list