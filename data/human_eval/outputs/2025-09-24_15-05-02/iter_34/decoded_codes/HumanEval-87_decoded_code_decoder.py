from typing import List, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    coordinates: List[Tuple[int, int]] = []
    for row_index in range(len(two_dimensional_list)):
        row = two_dimensional_list[row_index]
        for column_index in range(len(row)):
            if row[column_index] == target_integer:
                coordinates.append((row_index, column_index))
    # Sort by column descending, then by row ascending
    coordinates.sort(key=lambda x: x[1], reverse=True)
    coordinates.sort(key=lambda x: x[0])
    return coordinates