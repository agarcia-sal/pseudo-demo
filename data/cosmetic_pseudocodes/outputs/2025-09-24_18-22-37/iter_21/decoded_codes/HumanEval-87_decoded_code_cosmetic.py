from typing import List, Tuple, Any

def get_row(matrix: List[List[Any]], search_value: Any) -> List[Tuple[int, int]]:
    found_positions: List[Tuple[int, int]] = []
    outer_index: int = 0
    while outer_index <= len(matrix) - 1:
        inner_index: int = 0
        while inner_index <= len(matrix[outer_index]) - 1:
            if matrix[outer_index][inner_index] == search_value:
                found_positions.append((outer_index, inner_index))
            inner_index += 1
        outer_index += 1

    # Sort by second element descending (column), then by first element ascending (row)
    sorted_by_col_desc = sorted(found_positions, key=lambda x: x[1], reverse=True)
    final_sorted = sorted(sorted_by_col_desc, key=lambda x: x[0])

    return final_sorted