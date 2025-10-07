from typing import List, Tuple, Any

def get_row(list_of_lists: List[List[Any]], target_value: Any) -> List[Tuple[int, int]]:
    coordinates: List[Tuple[int, int]] = []
    for row_index, row in enumerate(list_of_lists):
        for col_index, value in enumerate(row):
            if value == target_value:
                coordinates.append((row_index, col_index))
    # Sort by col_index descending, then by row_index ascending
    coordinates.sort(key=lambda coord: coord[1], reverse=True)
    coordinates.sort(key=lambda coord: coord[0])
    return coordinates