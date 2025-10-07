from typing import List, Tuple, Any

def get_row(matrix: List[List[Any]], needle: Any) -> List[Tuple[int, int]]:
    found_positions: List[Tuple[int, int]] = []

    outer_index = 0
    while outer_index < len(matrix):
        inner_index = 0
        while inner_index < len(matrix[outer_index]):
            if not (matrix[outer_index][inner_index] != needle):
                found_positions.append((outer_index, inner_index))
            inner_index += 1
        outer_index += 1

    sorted_by_column_descending = sorted(found_positions, key=lambda pos: -pos[1])
    sorted_by_row_ascending = sorted(sorted_by_column_descending, key=lambda pos: pos[0])

    return sorted_by_row_ascending