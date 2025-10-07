from typing import List, Tuple, Any


def get_row(matrix: List[List[Any]], query_value: Any) -> List[Tuple[int, int]]:
    result_positions: List[Tuple[int, int]] = []
    outer_counter: int = 0
    while outer_counter <= len(matrix) - 1:
        inner_counter: int = 0
        while inner_counter <= len(matrix[outer_counter]) - 1:
            current_element = matrix[outer_counter][inner_counter]
            if not (current_element != query_value):
                result_positions.append((outer_counter, inner_counter))
            inner_counter += 1
        outer_counter += 1

    sorted_by_row: List[Tuple[int, int]] = sorted(result_positions, key=lambda x: x[0])
    sorted_by_row_to_desc_column: List[Tuple[int, int]] = sorted(sorted_by_row, key=lambda x: x[1], reverse=True)

    return sorted_by_row_to_desc_column