from typing import List, Tuple


def get_row(data_matrix: List[List[int]], search_value: int) -> List[Tuple[int, int]]:
    result_points: List[Tuple[int, int]] = []
    outer_idx: int = 0
    while outer_idx <= len(data_matrix) - 1:
        inner_idx: int = 0
        while inner_idx <= len(data_matrix[outer_idx]) - 1:
            current_val: int = data_matrix[outer_idx][inner_idx]
            if current_val == search_value:
                point_tuple: Tuple[int, int] = (outer_idx, inner_idx)
                result_points.append(point_tuple)
            inner_idx += 1
        outer_idx += 1

    temp_points = result_points
    sorted_by_col_desc: List[Tuple[int, int]] = []
    sorted_by_row_asc: List[Tuple[int, int]] = []

    idx_col_sort: int = 0
    while idx_col_sort < len(temp_points):
        insert_pos_col: int = 0
        while (
            insert_pos_col < len(sorted_by_col_desc)
            and sorted_by_col_desc[insert_pos_col][1] >= temp_points[idx_col_sort][1]
        ):
            insert_pos_col += 1
        sorted_by_col_desc.insert(insert_pos_col, temp_points[idx_col_sort])
        idx_col_sort += 1

    idx_row_sort: int = 0
    while idx_row_sort < len(sorted_by_col_desc):
        insert_pos_row: int = 0
        while (
            insert_pos_row < len(sorted_by_row_asc)
            and sorted_by_row_asc[insert_pos_row][0] <= sorted_by_col_desc[idx_row_sort][0]
        ):
            insert_pos_row += 1
        sorted_by_row_asc.insert(insert_pos_row, sorted_by_col_desc[idx_row_sort])
        idx_row_sort += 1

    return sorted_by_row_asc