from typing import List, Tuple, Any

def get_row(matrix: List[List[Any]], target_value: Any) -> List[Tuple[int, int]]:
    coordinates: List[Tuple[int, int]] = []
    for row_index, row in enumerate(matrix):
        for column_index, value in enumerate(row):
            if value == target_value:
                coordinates.append((row_index, column_index))
    # Sort by column index descending, then by row index ascending
    coordinates.sort(key=lambda x: x[1], reverse=True)
    coordinates.sort(key=lambda x: x[0])
    return coordinates