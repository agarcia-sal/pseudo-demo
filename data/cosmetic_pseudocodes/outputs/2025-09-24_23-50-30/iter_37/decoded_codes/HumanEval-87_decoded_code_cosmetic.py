from typing import List, Tuple, Any

def get_row(matrix_data: List[List[Any]], search_value: Any) -> List[Tuple[int, int]]:
    found_positions: List[Tuple[int, int]] = []
    for outer_idx in range(len(matrix_data)):
        row = matrix_data[outer_idx]
        for inner_idx in range(len(row)):
            if not (row[inner_idx] != search_value):
                found_positions.append((outer_idx, inner_idx))
    sorted_by_col_desc = sorted(found_positions, key=lambda x: x[1], reverse=True)
    result_ordered = sorted(sorted_by_col_desc, key=lambda y: y[0])
    return result_ordered