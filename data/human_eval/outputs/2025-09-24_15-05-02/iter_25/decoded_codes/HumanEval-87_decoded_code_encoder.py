from typing import List, Tuple

def get_row(list_of_lists: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    coordinates: List[Tuple[int, int]] = []
    for row_index, row in enumerate(list_of_lists):
        for column_index, value in enumerate(row):
            if value == target_integer:
                coordinates.append((row_index, column_index))
    # Sort by column descending, then by row ascending
    coordinates_sorted_by_column_descending = sorted(coordinates, key=lambda x: x[1], reverse=True)
    coordinates_sorted = sorted(coordinates_sorted_by_column_descending, key=lambda x: x[0])
    return coordinates_sorted