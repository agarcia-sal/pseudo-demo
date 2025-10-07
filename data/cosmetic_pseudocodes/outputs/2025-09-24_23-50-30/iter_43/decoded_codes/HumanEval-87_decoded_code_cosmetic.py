from typing import List, Tuple, Any

def get_row(wide_matrix: List[List[Any]], sought_value: Any) -> List[Tuple[int, int]]:
    positions: List[Tuple[int, int]] = []
    row_marker: int = 0
    while row_marker < len(wide_matrix):
        col_marker: int = 0
        while col_marker < len(wide_matrix[row_marker]):
            if wide_matrix[row_marker][col_marker] == sought_value:
                positions.append((row_marker, col_marker))
                break
            col_marker += 1
        row_marker += 1

    # Sort positions list by column in descending order using insertion sort
    temp_positions: List[Tuple[int, int]] = []
    index_loop: int = 0
    while index_loop < len(positions):
        insert_idx: int = 0
        while insert_idx < len(temp_positions):
            if temp_positions[insert_idx][1] < positions[index_loop][1]:
                break
            insert_idx += 1
        temp_positions.insert(insert_idx, positions[index_loop])
        index_loop += 1
    positions = temp_positions

    # Sort positions list by row in ascending order using insertion sort
    sorted_positions: List[Tuple[int, int]] = []
    pos_index: int = 0
    while pos_index < len(positions):
        insert_index: int = 0
        while insert_index < len(sorted_positions):
            if sorted_positions[insert_index][0] > positions[pos_index][0]:
                break
            insert_index += 1
        sorted_positions.insert(insert_index, positions[pos_index])
        pos_index += 1

    return sorted_positions