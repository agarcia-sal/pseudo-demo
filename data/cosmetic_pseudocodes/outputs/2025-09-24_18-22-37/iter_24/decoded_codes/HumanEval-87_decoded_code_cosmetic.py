from typing import List, Tuple, Any


def get_row(matrix_data: List[List[Any]], sought_value: Any) -> List[Tuple[int, int]]:
    result_positions: List[Tuple[int, int]] = []
    i = 0
    while i <= len(matrix_data) - 1:
        j = 0
        while j <= len(matrix_data[i]) - 1:
            if matrix_data[i][j] == sought_value:
                coord_pair = (i, j)
                result_positions.append(coord_pair)
                # found a match at this position; move on
                # note: original pseudocode breaks switch but continues loop
            j += 1
        i += 1
    # sort by col descending
    tmp_sorted_by_col = sorted(result_positions, key=lambda x: x[1], reverse=True)
    # then sort by row ascending
    tmp_sorted_by_row = sorted(tmp_sorted_by_col, key=lambda x: x[0])
    result_positions = tmp_sorted_by_row
    return result_positions