from typing import List, Tuple, Any

def get_row(matrix: List[List[Any]], value: Any) -> List[Tuple[int, int]]:
    result_positions: List[Tuple[int, int]] = []
    row_counter: int = 0
    while row_counter < len(matrix):
        col_counter: int = 0
        while col_counter < len(matrix[row_counter]):
            if matrix[row_counter][col_counter] == value:
                position_pair = (row_counter, col_counter)
                result_positions.append(position_pair)
            col_counter += 1
        row_counter += 1
    temp_sorted_desc = sorted(result_positions, key=lambda x: x[1], reverse=True)
    final_sorted = sorted(temp_sorted_desc, key=lambda x: x[0])
    return final_sorted