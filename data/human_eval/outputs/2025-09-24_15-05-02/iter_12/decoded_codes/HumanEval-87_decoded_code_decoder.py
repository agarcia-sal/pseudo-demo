from typing import List, Tuple, Any

def get_row(list_of_lists: List[List[Any]], target_value: Any) -> List[Tuple[int, int]]:
    coordinates: List[Tuple[int, int]] = []
    for row_index in range(len(list_of_lists)):
        for col_index in range(len(list_of_lists[row_index])):
            if list_of_lists[row_index][col_index] == target_value:
                coordinates.append((row_index, col_index))
    # Sort by second element (column) descending, then by first element (row) ascending
    coordinates.sort(key=lambda x: x[1], reverse=True)
    coordinates.sort(key=lambda x: x[0])
    return coordinates