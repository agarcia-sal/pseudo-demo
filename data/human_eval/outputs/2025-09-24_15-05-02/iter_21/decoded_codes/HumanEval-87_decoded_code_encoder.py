from typing import List, Tuple, Any

def get_row(list_of_lists: List[List[Any]], target_value: Any) -> List[Tuple[int, int]]:
    coordinates: List[Tuple[int, int]] = []
    for row_index in range(len(list_of_lists)):
        for column_index in range(len(list_of_lists[row_index])):
            if list_of_lists[row_index][column_index] == target_value:
                coordinates.append((row_index, column_index))
    # Sort by column descending
    coordinates.sort(key=lambda x: x[1], reverse=True)
    # Then sort by row ascending (stable sort ensures first sort is preserved within same row)
    coordinates.sort(key=lambda x: x[0])
    return coordinates